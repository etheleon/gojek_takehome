""" Downloads and formats data for API 1: TOTALTRIPS
"""

import re
from tempfile import NamedTemporaryFile

import pandas as pd

from gojek.util.gcs import upload_blob
from gojek.util.db import get_dataframe_from_bigquery


def get_trips_per_day(tables):
    """
    Gets trip per day

    Summarises the # of trips per day in each table and
    returns them as a concatenated pandas dataframe

    Parameters
    ------

    tables: list[str]
        list of table

    Returns
    ------
    pandas.DataFrame


    Example
    ------
    >>> tables = [
        'tlc_green_trips_2014','tlc_green_trips_2015',
        'tlc_green_trips_2016','tlc_green_trips_2017',
        'tlc_yellow_trips_2015','tlc_yellow_trips_2016',
        'tlc_yellow_trips_2017'
        ]
    >>> df = get_trips_per_day(tables)
    """
    query = """
        WITH num_pickups as (
            SELECT
            CAST(pickup_datetime AS date) as date,
            COUNT(*)  AS total_trips,
            {YEAR} AS year,
            '{COLOR}' AS color
        FROM
            `bigquery-public-data.new_york_taxi_trips.{TABLE}`
        GROUP BY CAST(pickup_datetime AS date)
        )
        SELECT * FROM num_pickups ORDER BY date
            """
    dfs = []
    for table in tables:
        (_, color, _, year) = re.split("_", table)
        dfs.append(
            get_dataframe_from_bigquery(
                query.format(TABLE=table, YEAR=year, COLOR=color)
            ))
    return (pd.concat(dfs)
            .loc[:, ['date', 'total_trips']]
            .groupby(['date'])
            .sum()
            .reset_index())


if __name__ == '__main__':

    AFILE = NamedTemporaryFile()
    BUCKET_NAME = "geoapi-assets"

    GREENS = "tlc_green_trips_{YEAR}"
    YELLOWS = "tlc_yellow_trips_{YEAR}"

    TABLES = [GREENS.format(YEAR=year) for year in [2014, 2015, 2016, 2017]]
    TABLES.extend([YELLOWS.format(YEAR=year) for year in [2015, 2016, 2017]])

    TOTALTRIPS = get_trips_per_day(TABLES)

    TOTALTRIPS.to_csv(AFILE.name, compression="gzip", index=False)

    upload_blob(BUCKET_NAME, AFILE.name, "total_trips.csv.gz")
