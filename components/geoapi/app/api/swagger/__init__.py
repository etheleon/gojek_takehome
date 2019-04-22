"""Swagger
"""

from flask_swagger_ui import get_swaggerui_blueprint
from dynaconf import settings


swagger = get_swaggerui_blueprint(
    '/v1/docs',
    f"http://{settings.SITENAME}/static/openapi.yml",
    config={'app_name': "Gojek Geo API"}
)
