WITH temp as (
SELECT
    DATE(dropoff_datetime) as date,
    trip_distance as miles,
    (trip_distance / NULLIF(DATETIME_DIFF(dropoff_datetime, pickup_datetime, SECOND), 0)) AS MPS
FROM (
  SELECT
    trip_distance, dropoff_datetime, pickup_datetime
  FROM
    `bigquery-public-data.new_york_taxi_trips.tlc_green_trips_2014` UNION ALL
  SELECT
    trip_distance, dropoff_datetime, pickup_datetime
  FROM
    `bigquery-public-data.new_york_taxi_trips.tlc_green_trips_2015` UNION ALL
  SELECT
    trip_distance, dropoff_datetime, pickup_datetime
  FROM
    `bigquery-public-data.new_york_taxi_trips.tlc_yellow_trips_2015` UNION ALL
  SELECT
    trip_distance, dropoff_datetime, pickup_datetime
  FROM
    `bigquery-public-data.new_york_taxi_trips.tlc_yellow_trips_2016` )
WHERE
    dropoff_datetime is not NULL
    AND pickup_datetime is not NULL
    AND trip_distance is not NULL
)
SELECT
    date,
    AVG(MPS) as average_speed
FROM temp
GROUP BY date
ORDER BY date
