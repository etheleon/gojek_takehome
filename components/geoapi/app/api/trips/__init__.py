"""API for total trips
"""

import json

from flask import Blueprint, current_app
import pandas as pd

trips = Blueprint('trips', __name__)  # pylint: disable=invalid-name


@trips.route('/total_trips')
def get_trips(start='2016-01-01', end='2016-01-10'):
    """Returns total trips
    """

    def format_date(series):
        """Format days"""
        return series.apply(lambda day: day.strftime("%Y-%m-%d"))

    firstdate = pd.to_datetime(start).date()
    lastdate = pd.to_datetime(end).date()
    all_trips = (current_app.trips["total_trips"]
                 .query('@firstdate <= date < @lastdate')
                 .loc[:, ['date', 'total_trips']]
                 .assign(date=lambda df: format_date(df["date"])))
    return json.dumps(all_trips.to_dict(orient='records'))

@trips.route('/average_speed_24hrs')
def get_ave_speed(date):
    """Returns average speed of vehicles in a day
    """
    print("done")
