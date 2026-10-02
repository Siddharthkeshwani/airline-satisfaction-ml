-- Total rows
select count(*) as total_rows 
from airline_passenger_satisfaction;


-- missing arrival delays
select count(*) as mssing_arrival_delay
from airline_passenger_satisfaction
where arrival_delay is null;


-- target split
select satisfaction, count(*) as passengers
from airline_passenger_satisfaction
group by satisfaction
order by passengers DESC;


-- ID range
select min(id) as min_id, max(id) as max_id
from airline_passenger_satisfaction;


-- Number and range checks
select min(age) as min_age, max(age) as max_age,
       min(flight_distance) as min_distance, max(flight_distance) as max_distance,
       max(departue_delay) as max_departure_delay, max(arrival_delay) as max_arrival_delay
from airline_passenger_satisfaction;


-- category counts
select travel_class, count(*) as passengers
from airline_passenger_satisfaction
group by travel_class
order by passengers desc;


-- wifi ratings
select inflight_wifi_service as wifi_rating, count(*) as passengers
from airline_passenger_satisfaction
group by inflight_wifi_service
order by inflight_wifi_service;