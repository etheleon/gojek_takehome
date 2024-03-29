"""Stores settings
"""

import os

BIGQUERY_DATASET = os.environ.get("BIGQUERY_DATASET", "gpsprice")
BIGQUERY_BUCKET = os.environ.get("BIGQUERY_BUCKET", "bigquery_output_gojek")
GCP_PROJECT = os.environ.get("GCP_PROJECT", "datascience-237903")

ASSETS = {
    "BUCKET": os.environ.get("ASSSETS_BUCKET", "geoapi-assets"),
    "LOCAL_DIR": os.environ.get("ASSETS_DIR", "/geoapi/app/assets"),
    "TOTAL_TRIPS": os.environ.get("TOTAL_TRIPS", "total_trips.csv.gz"),
    "FARE": os.environ.get("FARE", "fare_heatmap.csv.gz"),
    "AVESPEED": os.environ.get("AVESPEED", "trips_ave_speed.csv.gz")
}
