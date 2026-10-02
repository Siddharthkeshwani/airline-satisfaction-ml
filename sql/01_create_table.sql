DROP TABLE IF EXISTS airline_passenger_satisfaction;

CREATE TABLE airline_passenger_satisfaction (
    
    id              INTEGER PRIMARY KEY,

    gender          VARCHAR(10),
    age             SMALLINT,
    customer_type   VARCHAR(15),
    type_of_travel  VARCHAR(15),
    travel_class    VARCHAR(15),
    flight_distance INTEGER,
    departure_delay INTEGER,
    arrival_delay   INTEGER,
    departure_arrival_time_convenience SMALLINT,
    ease_of_online_booking             SMALLINT,
    checkin_service                    SMALLINT,
    online_boarding                    SMALLINT,
    gate_location                      SMALLINT,
    onboard_service                    SMALLINT,
    seat_comfort                       SMALLINT,
    leg_room_service                   SMALLINT,
    cleanliness                        SMALLINT,
    food_and_drink                     SMALLINT,
    inflight_service                   SMALLINT,
    inflight_wifi_service              SMALLINT,
    inflight_entertainment             SMALLINT,
    baggage_handling                   SMALLINT,
    satisfaction                       VARCHAR(30)
);