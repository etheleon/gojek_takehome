#!/usr/bin/env python
"""Module for computing input data
"""

import logging
from os.path import join
from tempfile import NamedTemporaryFile
import pkg_resources

import pandas as pd

from dynaconf import settings

from gojek.util.gcs import upload_blob
from gojek.util.db import get_dataframe_from_bigquery
from gojek.util.geo import compute_ave_fare

__version__ = "0.0.1"

LOGGER = logging.getLogger("compute")
LOGGER.setLevel(logging.DEBUG)

GREEN_YEARS = [
    2014,
    2015,
    2016,
    2017
]
YELLOW_YEARS = [
    2015,
    2016,
    2017
]

TABLES = [f"bigquery-public-data.new_york_taxi_trips.{t}" for t in
          [f"tlc_green_trips_{yr}" for yr in GREEN_YEARS] +
          [f"tlc_yellow_trips_{yr}" for yr in YELLOW_YEARS]]


def save_to_gcs(df, file, bucket=settings.ASSETS.BUCKET):
    """saves dataframe to GCS"""
    output_file = NamedTemporaryFile().name
    df.to_csv(output_file, compression="gzip", index=False)
    upload_blob(bucket, output_file, file)


def read_sql(name="total_trips.sql"):
    """Reads SQL
    >>> read_sql("total_trips.sql")
    """
    template = pkg_resources.resource_filename("gojek", join("sql", name))
    with open(template, 'r') as myfile:
        query = myfile.read()
    return query


class Compute:
    """Module for computing data for gojek takehome APIs
    """
    def __init__(self):
        """Stores table info as attr"""
        self.tables = pd.DataFrame({
            "tables": TABLES,
            "year": GREEN_YEARS + YELLOW_YEARS,
            "color": ["green" for i in GREEN_YEARS] +
                     ["yellow" for i in YELLOW_YEARS]
        })

    def trips_per_day(self):
        """Calculates the average speed"""
        dfs = []
        for _, row in self.tables.iterrows():
            tbl, yr, col = row["tables"], row["year"], row["color"]
            LOGGER.info("Processing %s", tbl)
            query = (read_sql("total_trips.sql")
                     .format(TABLE=tbl, YEAR=yr, COLOR=col))
            query = query.replace("\n", " ")
            dfs.append(get_dataframe_from_bigquery(query))
        (pd.concat(dfs)
         .loc[:, ['date', 'total_trips']]
         .groupby(['date']).sum()
         .reset_index()  # .head())
         .pipe(save_to_gcs, settings.ASSETS.FILES.TOTAL_TRIPS))

    def fare_heatmaps(self):
        """Calculates the fares"""
        valids = []
        for _, row in self.tables.iterrows():
            tbl, yr, col = row["tables"], row["year"], row["color"]
            LOGGER.info("Processing %s", tbl)
            try:
                compute_ave_fare(tbl, yr, col)
                valids.append(f"{col}-{yr}.csv.gz")
            except Exception as err:  # pylint: disable=broad-except
                LOGGER.warning(f"Error {yr}-{col}: {err}")

        (pd.concat([pd.read_csv(csv, compression="gzip") for csv in valids])
         .groupby(["date", "s2id"]).mean()
         .reset_index()
	 .rename(columns={"total_amount":"fare"})
         .pipe(save_to_gcs, settings.ASSETS.FILES.FARE))

    def average_speed(self):  # pylint: disable=no-self-use
        """Calculates the average speed for every day"""
        query = read_sql("ave_speed.sql")
        ave_speed_df = get_dataframe_from_bigquery(query, multipart=True)
        ave_speed_df.pipe(save_to_gcs, settings.ASSETS.FILES.AVESPEED)
