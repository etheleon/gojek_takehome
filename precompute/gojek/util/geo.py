"""geolocation related function
"""

# import gc

import logging

import s2sphere
import pandas as pd
from tqdm import tqdm

LOGGER = logging.getLogger("utils")
LOGGER.setLevel(logging.DEBUG)


def latlng_to_s2cellid(lat, long):
    """
    This function converts latlng coordinates to s2cell ids
    """
    try:
        position = s2sphere.LatLng.from_degrees(lat, long)
        return str(s2sphere.CellId.from_lat_lng(position).parent(16))
    except Exception as err:  # pylint: disable=broad-except
        # LOGGER.warning(f"Error: {err}")
        return None


def compute_ave_fare(df):  # pylint: disable=invalid-name
    """ Computes ave fair
    Things to do:
    1. I need to know the memory consumption
    2. I need to know the intermediate memory consumption
    """
    latlongs = []
    for _, row in tqdm(df.iterrows(), total=df.shape[0], desc="LatLong"):
        latlongs.append(latlng_to_s2cellid(row.pickup_latitude,
                                           row.pickup_longitude))
    cellids = pd.Series(latlongs, dtype="category")
    del latlongs
    # gc.collect()
    # return (df
    #         .loc[:, ["date", "total_amount"]]
    #         .assign(cellid=cellids)
    #         .groupby(["date", "cellid"])
    #         .mean()
    #         .dropna())
    return cellids
