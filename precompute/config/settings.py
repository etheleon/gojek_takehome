import os

BIGQUERY_DATASET = os.environ.get('BIGQUERY_DATASET',"gpsprice")
BIGQUERY_BUCKET = os.environ.get('BIGQUERY_BUCKET',"bigquery_output_gojek")
GCP_PROJECT = os.environ.get('GCP_PROJECT',"datascience-237903")

ASSETS = {
    "BUCKET": "geoapi-assets",
    "FILES": {
        "TOTAL_TRIPS": "total_trips.csv.gz",
        "FARE": "fare_heatmap.csv.gz",
        "AVESPEED":"trips_ave_speed.csv.gz"
    }
}
