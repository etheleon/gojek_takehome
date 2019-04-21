"""Utility functions
"""

import logging
import os
from os.path import join
import re
import time
import uuid

import dask.dataframe as dd
from google.cloud import bigquery
from google.cloud import storage

client = bigquery.Client()  # pylint: disable=invalid-name
storage_client = storage.Client()  # pylint: disable=invalid-name

logger = logging.getLogger('gojek_utils')  # pylint: disable=invalid-name
logger.setLevel(logging.INFO)

PROJECT = os.environ["GCP_PROJECT"]
BQ_DATASET = os.environ["BIGQUERY_DATASET"]
BUCKET_NAME = os.environ["BIGQUERY_BUCKET"]
TEMPFILE = "gs://{BUCKET_NAME}/{FILENAME}-*.csv.gz"


def execute_query(query, destination_table=None, location='US'):
    """
    destination_table : ref
        refers to the destination table
    """
    job_config = bigquery.QueryJobConfig()
    if destination_table is not None:
        job_config.destination = destination_table
    job = client.query(
        query,
        location=location,
        job_config=job_config)
    logger.info("Executing query...")
    while job.state != 'DONE':
        job.reload()
        time.sleep(5)
    err = job.error_result
    if err is not None:
        logger.warning("Not_Sucessful %s", err)
        return False
    logger.info("Complete")
    return True


def save_table_to_gcs(table_ref, destination_uri, gzip=True, location='US'):
    """saves table to google cloud storage
    """
    job_config = bigquery.job.ExtractJobConfig()
    if gzip:
        job_config.compression = 'GZIP'
    job = client.extract_table(
        table_ref,
        destination_uri,
        location=location,
        job_config=job_config
    )
    logger.info("Saving table to GCS...")
    while job.state != 'DONE':
        time.sleep(5)
        job.reload()
    err = job.error_result
    if err is not None:
        logger.warning("Not_Sucessful %s", err)
        return False
    logger.info("Complete")
    return True


def save_query_to_gzip(query, location="US"):
    """
    When the tables are too big,
    using the conventional method might be too slow

    Parameters
    ------

    """

    temp_name = str(uuid.uuid4())

    destination_uri = TEMPFILE.format(
        BUCKET_NAME=BUCKET_NAME,
        FILENAME=temp_name)
    table_name = re.sub("-", "_", temp_name)
    dataset_id = f"{PROJECT}.{BQ_DATASET}"
    full_id = f"{dataset_id}.{table_name}"
    dataset = bigquery.Dataset(dataset_id)
    dataset.location = location
    dataset = client.create_dataset(dataset, exists_ok=True)
    table_ref = client.dataset(BQ_DATASET).table(table_name)
    query_completed = execute_query(query, destination_table=table_ref,
                                    location=location)
    if query_completed:
        table_saved = save_table_to_gcs(table_ref, destination_uri,
                                        location=location)
    if table_saved:
        return destination_uri, full_id
    return None, None


def get_dataframe_from_bigquery(query, is_big=False,
                                location='US', as_pandas=False):
    """ downloads query as pandas dataframe
    """
    if is_big:
        destination_uri, full_id = save_query_to_gzip(query, location=location)
        regex_pattern = re.split(
            r"\*", re.split(r"/", destination_uri).pop()
        ).pop(0)

        bucket = storage_client.get_bucket(BUCKET_NAME)

        blobs = bucket.list_blobs()
        for blob in blobs:
            if re.search(regex_pattern, blob.name) is not None:
                file = join("/tmp", blob.name)
                blob.download_to_filename(file)
                blob.delete()

        query_df = dd.read_csv(join("/tmp", f"{regex_pattern}*"),
                               compression='gzip')
        if as_pandas:
            query_df = query_df.as_pandas()
        client.delete_table(full_id, not_found_ok=True)
    else:
        query_df = client.query(query).to_dataframe()
    return query_df
