import json
from pathlib import Path

import joblib
import pandas as pd
import streamlit as st

# the models folder sits next to the app folder
MODEL_FOLDER = Path(__file__).resolve().parent.parent / "models"

st.set_page_config(page_title="Airline passenger satisfaction")


@st.cache_resource
def load_models():
    # runs once, then Streamlit remembers the result
    with open(MODEL_FOLDER / "model_info.json") as file:
        info = json.load(file)

    model_wifi = joblib.load(MODEL_FOLDER / info["with_wifi"]["file"])
    model_no_wifi = joblib.load(MODEL_FOLDER / info["without_wifi"]["file"])
    return info, model_wifi, model_no_wifi


info, model_wifi, model_no_wifi = load_models()

st.title("Airline passenger satisfaction")
st.write("Describe a passenger and their flight. The model estimates the chance that the passenger was satisfied.")
st.caption("A portfolio project. It estimates satisfaction from ratings given in the same survey, so it shows what goes with "
           "satisfaction. It does not forecast how someone will feel in advance.")

# ---------- the form ----------
st.subheader("The passenger and the flight")

left, right = st.columns(2)

with left:
    customer_type = st.selectbox("Customer type", ["Returning", "First-time"])
    type_of_travel = st.selectbox("Type of travel", ["Business", "Personal"])
    travel_class = st.selectbox("Class", ["Business", "Economy", "Economy Plus"])

with right:
    age = st.slider("Age", 7, 85, 40)
    flight_distance = st.number_input("Flight distance (miles)", min_value=31, max_value=4983, value=1000)
    departure_delay = st.number_input("Departure delay (minutes)", min_value=0, max_value=1592, value=0)

st.subheader("Ratings")
st.caption("0 means not applicable, 5 means excellent.")

rating_labels = {
    "ease_of_online_booking": "Ease of online booking",
    "checkin_service": "Check-in service",
    "online_boarding": "Online boarding",
    "onboard_service": "On-board service",
    "seat_comfort": "Seat comfort",
    "leg_room_service": "Leg room",
    "cleanliness": "Cleanliness",
    "food_and_drink": "Food and drink",
    "inflight_service": "In-flight service",
    "inflight_entertainment": "In-flight entertainment",
    "baggage_handling": "Baggage handling (1 to 5)",
}

ratings = {}
for column, label in rating_labels.items():
    lowest = 1 if column == "baggage_handling" else 0
    ratings[column] = st.slider(label, lowest, 5, 3)

# ---------- the wifi switch ----------
use_wifi = st.checkbox("Also use the in-flight wifi rating")

if use_wifi:
    wifi_rating = st.slider("In-flight wifi service", 0, 5, 3)

with st.expander("Why is wifi a switch?"):
    st.write(
        "In the data this model learned from, passengers who gave the wifi a 0 or a 5 were almost all satisfied "
        "(about 99%), far more than for any other rating. That looks like a quirk of the dataset, not real "
        "behaviour. Using wifi makes the model more accurate on this dataset "
        f"({info['with_wifi']['test_accuracy']:.1f}% against {info['without_wifi']['test_accuracy']:.1f}%), "
        "but a single rating can then swing the answer. So wifi is off by default."
    )

# ---------- the prediction ----------
if st.button("Predict"):
    passenger = {
        "customer_type": customer_type,
        "type_of_travel": type_of_travel,
        "travel_class": travel_class,
        "age": age,
        "flight_distance": flight_distance,
        "departure_delay": departure_delay,
    }
    passenger.update(ratings)

    if use_wifi:
        passenger["inflight_wifi_service"] = wifi_rating
        model = model_wifi
        columns = info["with_wifi"]["columns"]
        accuracy = info["with_wifi"]["test_accuracy"]
    else:
        model = model_no_wifi
        columns = info["without_wifi"]["columns"]
        accuracy = info["without_wifi"]["test_accuracy"]

    passenger = pd.DataFrame([passenger])
    chance = model.predict_proba(passenger[columns])[0, 1]

    st.subheader("Result")
    st.metric("Chance of satisfied", f"{chance * 100:.1f}%")

    if chance >= 0.5:
        st.success("The model predicts: satisfied")
    else:
        st.info("The model predicts: neutral or dissatisfied")

    if 0.3 <= chance <= 0.7:
        st.warning("This is a close call. The model is less sure here, and borderline cases are where it makes most of its mistakes.")

    st.caption(f"On 25,976 passengers it had never seen, this version was right {accuracy:.1f}% of the time.")

    with st.expander("What the model received"):
        st.dataframe(passenger[columns])
        