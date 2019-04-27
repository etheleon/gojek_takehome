"""geolocation related function
"""

# import gc

import logging
import subprocess
from tempfile import NamedTemporaryFile

import pandas as pd

from gojek.util.db import get_dataframe_from_bigquery
from gojek.util.misc import timeit

LOGGER = logging.getLogger("geo")
LOGGER.setLevel(logging.DEBUG)


@timeit
def compute_s2id(df, color, year):
    """ Computes s2id from latlng
    """
    LOGGER.info(f"Processing: {color} {year}")
    date_latlng_fare = NamedTemporaryFile().name
    date_s2id_fare = NamedTemporaryFile().name
    df.to_csv(date_latlng_fare, index=False)
    with open(date_s2id_fare, "w") as fh:
        subprocess.call(["latlng2s2", date_latlng_fare], stdout=fh)
    return pd.read_csv(date_s2id_fare, header=None,
                       names=["date", "s2id", "total_amount"])


def compute_ave_fare(table, year, color):
    """computes ave fare per s2 cell
    """

    query = '''
    SELECT
        cast(pickup_datetime AS date) AS date,
        pickup_latitude,
        pickup_longitude,
        total_amount
    FROM
        `{TABLE}`
    WHERE
        pickup_latitude IS NOT NULL
        AND pickup_longitude IS NOT NULL
        AND total_amount IS NOT NULL
            '''.format(TABLE=table)

    df = get_dataframe_from_bigquery(query, multipart=True)

    if df.empty:
        raise Exception("no records")

    (compute_s2id(df, color, year)
     .groupby(["date", "s2id"])
     .mean()
     .dropna()
     .reset_index()
     .rename({"total_amount": "ave_fare"})
     .to_csv(f"{color}-{year}.csv.gz", compression="gzip", index=False))
