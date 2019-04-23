"""geolocation related function
"""

import gc

import s2sphere
import pandas as pd


def latlng_to_s2cellid(lat, long):
    """
    This function converts latlng coordinates to s2cell ids
    """
    position = s2sphere.LatLng.from_degrees(lat, long)
    return str(s2sphere.CellId.from_lat_lng(position).parent(16))


def compute_ave_fare(df):  # pylint: disable=invalid-name
    """ Computes ave fair
    Things to do:
    1. I need to know the memory consumption
    2. I need to know the intermediate memory consumption
    """
    latlongs = []
    for _, row in df.iterrows():
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
