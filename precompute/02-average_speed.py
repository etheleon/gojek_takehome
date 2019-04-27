#!/usr/bin/env python

""" Downloads and formats data for API 3

from gojek.util.db import get_dataframe_from_bigquery

ave_speed_df = get_dataframe_from_bigquery("""
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
""", multipart=True)

ave_speed_df.to_csv("data/trip_ave_speed.csv.bz2")
