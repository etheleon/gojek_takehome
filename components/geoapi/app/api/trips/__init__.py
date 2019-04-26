"""API for total trips
"""

import json

from flask import Blueprint, current_app
import pandas as pd

from webargs import fields
from webargs.flaskparser import use_args

trips = Blueprint('trips', __name__)  # pylint: disable=invalid-name


@trips.route('/total_trips')
@use_args({
    "start": fields.Str(missing='2016-01-01'),  # pylint: disable=no-member
    "end": fields.Str(missing='2016-01-10')  # pylint: disable=no-member
})  # pylint: disable=E1101
def get_trips(args):
    """Returns total trips
    """

    def format_date(series):
        """Format days"""
        return series.apply(lambda day: day.strftime("%Y-%m-%d"))

    firstdate = pd.to_datetime(args["start"]).date()
    lastdate = pd.to_datetime(args["end"]).date()
    all_trips = (current_app.trips["total_trips"]
                 .query('@firstdate <= date < @lastdate')
                 .loc[:, ['date', 'total_trips']]
                 .assign(date=lambda df: format_date(df["date"])))
    return json.dumps(all_trips.to_dict(orient='records'))


@trips.route('/average_speed_24hrs')
@use_args({
    "date": fields.Str(missing='2016-01-01'),  # pylint: disable=no-member
})
def get_ave_speed(args):
    """Returns average speed of vehicles in a day
    """
    mock_output = [{"average_speed": 24.7}]
    return json.dumps(mock_output)
