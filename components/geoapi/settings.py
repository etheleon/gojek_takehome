"""Stores settings
"""

import os

BIGQUERY_DATASET = os.environ.get("BIGQUERY_DATASET", "gpsprice")
BIGQUERY_BUCKET = os.environ.get("BIGQUERY_BUCKET", "bigquery_output_gojek")
GCP_PROJECT = os.environ.get("GCP_PROJECT", "datascience-237903")

ASSETS = {
    "BUCKET": os.environ.get("ASSSETS_BUCKET", "geoapi-assets"),
    "LOCAL_DIR": os.environ.get("ASSETS_DIR", "/geoapi/app/assets")
}
