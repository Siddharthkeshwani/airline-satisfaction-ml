ID_COL = "id"
TARGET_COL = "satisfaction"
POSITIVE_CLASS = "Satisfied"


# text columns with few fixed values
CATEGORICAL_COLS = [
    "gender",
    "customer_type",
    "type_of_travel",
    "travel_class",
]


# Real measurements 
NUMERIC_COLS = [
    "age",
    "flight_distance",
    "departure_delay",
    "arrival_delay",
]

# Ratings are on a scale of 1-5
RATING_COLS = [
    "departure_arrival_time_convenience",
    "ease_of_online_booking",
    "checkin_service",
    "online_boarding",
    "gate_location",
    "onboard_service",
    "seat_comfort",
    "leg_room_service",
    "cleanliness",
    "food_and_drink",
    "inflight_service",
    "inflight_wifi_service",
    "inflight_entertainment",
    "baggage_handling",
]

