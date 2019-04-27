""" GeoAPI
"""

from flask import (
    Flask,
    jsonify,
    make_response
)


from api.heartbeat import heartbeat
from api.trips import trips
from api.fare import fare
from api.swagger import swagger

from utils.data import (
    load_total_trips,
    load_fare,
    load_ave_speed
)

BLUEPRINTS = [
    (trips, ['/v1']),
    (fare, ['/v1']),
    (swagger, ['/v1/docs'])
]


def create_app():
    """Application Factory"""
    app = Flask(__name__,
                static_url_path="/static")

    app.trips = {
        "total_trips": load_total_trips(),
        "ave_speed": load_ave_speed()
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
