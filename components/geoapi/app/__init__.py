from flask import (
    Flask,
    jsonify,
    make_response
)

from dynaconf import settings

from api.heartbeat import heartbeat_blueprint
from api.total_trips import total_trips_blueprint
from api.fare_heatmap import fare_heatmap_blueprint
from api.ave_speed import ave_speed_blueprint
from api.swagger import swagger_blueprint
from flask_swagger_ui import get_swaggerui_blueprint


BLUEPRINTS = [
    (total_trips_blueprint, ['/v1']),
    (fare_heatmap_blueprint, ['/v1']),
    (ave_speed_blueprint, ['/v1']),
    (swagger_blueprint, ['/v1/docs'])
]

def create_app():
    app = Flask(__name__, static_url_path="/static")


    # Heartbeat API
    app.register_blueprint(heartbeat_blueprint)

    # Additional
    for blueprint, prefixes in BLUEPRINTS:
        for prefix in prefixes:
            app.register_blueprint(blueprint, url_prefix=prefix)
    @app.errorhandler(404)
    def not_found(error):
        return make_response(jsonify({'error': 'Not found'}), 404)

    return app

app = create_app()
