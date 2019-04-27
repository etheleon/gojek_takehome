""" loads models
"""

from os.path import join
import logging

from dynaconf import settings
import pandas as pd

from utils.gcs import download_blob

LOGGER = logging.getLogger('gunicorn.error')


def load_total_trips():
    """loads total trips csv
    """
    try:
        download_blob(settings.ASSETS.BUCKET,
                      "total_trips.csv.gz",
                      join(settings.ASSETS.LOCAL_DIR,
                           settings.ASSETS.TOTAL_TRIPS))
    except Exception as err:  # pylint: disable=broad-except
        LOGGER.warning(f"Failed Downloading total_trips: {err}")

    try:
        df = pd.read_csv(join(settings.ASSETS.LOCAL_DIR,
                              settings.ASSETS.TOTAL_TRIPS),
                         compression="gzip")
        df["date"] = pd.to_datetime(df["date"], format="%Y-%m-%d")
    except FileNotFoundError as err:
        LOGGER.warning(f"Failed reading total trips data: {err}")
        df = None
    return df

def load_fare():
    """loads fare prices
    """
    try:
        download_blob(settings.ASSETS.BUCKET,
                      settings.ASSETS.FARE,
                      join(settings.ASSETS.LOCAL_DIR,
                           settings.ASSETS.FARE))
    except Exception as err:  # pylint: disable=broad-except
        LOGGER.warning(f"Failed Downloading Fare: {err}")
    try:
        df = pd.read_csv(join(settings.ASSETS.LOCAL_DIR,
                              settings.ASSETS.FARE),
                         compression="gzip")
        df["date"] = pd.to_datetime(df["date"], format="%Y-%m-%d")
    except FileNotFoundError as err:
        LOGGER.warning(f"Failed reading fare data: {err}")
        df = None
    return df

def load_ave_speed():
    """loads fare prices
    """
    try:
        download_blob(settings.ASSETS.BUCKET,
                      settings.ASSETS.AVESPEED,
                      join(settings.ASSETS.LOCAL_DIR,
                           settings.ASSETS.AVESPEED))
    except Exception as err:  # pylint: disable=broad-except
        LOGGER.warning(f"Failed Downloading Fare: {err}")
    try:
        df = pd.read_csv(join(settings.ASSETS.LOCAL_DIR,
                              settings.ASSETS.AVESPEED),
                         compression="gzip")
        df["date"] = pd.to_datetime(df["date"], format="%Y-%m-%d")
    except FileNotFoundError as err:
        LOGGER.warning(f"Failed reading fare data: {err}")
        df = None
    return df
