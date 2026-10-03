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



# text columns (encoded in Step 8)
MODEL_TEXT_COLS = [
    "customer_type",
    "type_of_travel",
    "travel_class",
]

# number columns
MODEL_NUMBER_COLS = [
    "age",
    "flight_distance",
    "departure_delay",
]

# survey ratings we keep (gate_location and departure_arrival_time_convenience are dropped)
MODEL_RATING_COLS = [
    "ease_of_online_booking",
    "checkin_service",
    "online_boarding",
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

# the same ratings without wifi
MODEL_RATING_COLS_NO_WIFI = [
    "ease_of_online_booking",
    "checkin_service",
    "online_boarding",
    "onboard_service",
    "seat_comfort",
    "leg_room_service",
    "cleanliness",
    "food_and_drink",
    "inflight_service",
    "inflight_entertainment",
    "baggage_handling",
]

# the full feature lists (18 columns with wifi, 17 without)
FEATURE_COLS = MODEL_TEXT_COLS + MODEL_NUMBER_COLS + MODEL_RATING_COLS
FEATURE_COLS_NO_WIFI = MODEL_TEXT_COLS + MODEL_NUMBER_COLS + MODEL_RATING_COLS_NO_WIFI