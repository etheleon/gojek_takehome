import os

BIGQUERY_DATASET=os.environ.get("GOJEK_DATASET", "gpsprice")
BIGQUERY_BUCKET=os.environ.get("BUCKET", "bigquery_output_gojek")
GCP_PROJECT=os.environ.get("PROJECT_ID", "datascience-237903")
ASSETS_DIR=os.environ.get("ASSETS", "/Users/m179-hb/github/gojek_takehome/components/geoapi/app/assets")
