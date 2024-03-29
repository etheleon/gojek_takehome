"""API for total trips
"""

from flask import (
    Blueprint,
    current_app,
    jsonify
)
import pandas as pd

from webargs import fields
from webargs.flaskparser import use_args

trips = Blueprint('trips', __name__)  # pylint: disable=invalid-name


def format_date(series):
    """Format days"""
    return series.apply(lambda day: day.strftime("%Y-%m-%d"))

@trips.route('/total_trips')
@use_args({
    "start": fields.Date(missing='2016-01-01', format='%Y-%m-%d'),  # pylint: disable=no-member
    "end": fields.Date(missing='2016-01-10', format='%Y-%m-%d')  # pylint: disable=no-member
})  # pylint: disable=E1101
def get_trips(args):
    """Returns total trips
    """


    firstdate = pd.to_datetime(args["start"]).date()  # noqa: F841
    lastdate = pd.to_datetime(args["end"]).date()  # noqa: F841
    all_trips = (current_app.trips["total_trips"]
                 .query('@firstdate <= date < @lastdate')
                 .loc[:, ['date', 'total_trips']]
                 .assign(date=lambda df: format_date(df["date"])))
    return jsonify(all_trips.to_dict(orient='records'))


@trips.route('/average_speed_24hrs')
@use_args({
    "date": fields.Date(format='%Y-%m-%d', missing='2016-01-01'),  # pylint: disable=no-member
})
def get_ave_speed(args):
    """Returns average speed of vehicles in a day
    """
    date = args["date"]  # pylint: disable=unused-variable
    records = (current_app.trips["ave_speed"]
               .query("date == @date")
               .assign(date=lambda df: format_date(df["date"])))
    return jsonify(records.to_dict(orient='records'))
