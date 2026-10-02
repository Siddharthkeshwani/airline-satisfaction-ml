TRUNCATE TABLE airline_passenger_satisfaction;

\copy airline_passenger_satisfaction FROM 'data/raw/airline_passenger_satisfaction.csv' with (FORMAT csv, HEADER true)
