""" GeoAPI
"""

from os.path import join
import logging
from flask import (
    Flask,
    jsonify,
    make_response
)
import pandas as pd

from dynaconf import settings

from api.heartbeat import heartbeat
from api.trips import trips
from api.fare import fare
from api.swagger import swagger


from utils.gcs import download_blob

BLUEPRINTS = [
    (trips, ['/v1']),
    (fare, ['/v1']),
    (swagger, ['/v1/docs'])
]

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
                           settings.ASSETS.ASSETS.FARE))
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

def create_app():
    """Application Factory"""
    app = Flask(__name__,
                static_url_path="/static")

    app.trips = {
        "total_trips": load_total_trips()
    }
    app.fare = {
        "heatmap" : load_fare()
    }
    app.register_blueprint(heartbeat)

    # Additional
    for blueprint, prefixes in BLUEPRINTS:
        for prefix in prefixes:
            app.register_blueprint(blueprint, url_prefix=prefix)

    @app.errorhandler(404)
    def not_found(error):  # pylint: disable=unused-variable
        """doc string"""
        return make_response(jsonify({'error': f'Not found: {error}'}), 404)

    return app


app = create_app()
