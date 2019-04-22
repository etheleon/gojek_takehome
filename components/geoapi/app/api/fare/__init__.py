"""Returns fare
"""


import json

from flask import Blueprint, current_app
import pandas as pd

fare = Blueprint('fare', __name__)  # pylint: disable=invalid-name


@fare.route("/average_fare_heatmap")
def get_average_fare():
    """docstring"""
    print("done")
