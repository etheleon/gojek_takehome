from flask import Blueprint

heartbeat = Blueprint('heartbeat', __name__)


@heartbeat.route('/heartbeat', methods=['GET'])
def get_heartbeat_api():
    return 'ok'
