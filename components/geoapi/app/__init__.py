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


def load_total_trips():
    """loads total trips csv
    """
    try:
        download_blob(settings.BUCKET,
                      "total_trips.csv.gz",
                      join(settings.ASSETS_DIR, "total_trips.csv.gz"))
    except:
        logging.warning("No such csv")

    try:
        df = pd.read_csv(join(settings.ASSETS_DIR, "total_trips.csv.gzip"),
                         compression="gzip")
        df["date"] = pd.to_datetime(df["date"], format="%Y-%m-%d")
    except FileNotFoundError:
        logging.warning("Failed loading csv")
        df = None
    return df


def create_app():
    """Application Factory"""
    app = Flask(__name__,
                static_url_path="/static")

    df = load_total_trips()
    app.trips = {
        "total_trips": df
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
