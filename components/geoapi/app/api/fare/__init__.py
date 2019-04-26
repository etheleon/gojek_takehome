"""Returns fare
"""


import json

from flask import Blueprint, current_app
import pandas as pd

from webargs import fields
from webargs.flaskparser import use_args

fare = Blueprint('fare', __name__)  # pylint: disable=invalid-name


@fare.route("/average_fare_heatmap")
@use_args({
    "date": fields.Str(missing='2016-01-01'),  # pylint: disable=E1101
})  # pylint: disable=E1101
def get_average_fare(args):
    """fare heatmap
    """

    date = pd.to_datetime(args["date"]).date()
    # current_app.fare

    mock_output = [
      {
         "s2id":"951977d37",
         "fare":13.21
      },
      {
         "s2id":"951977d39",
         "fare":4.32
      },
      {
         "s2id":"951977d40",
         "fare":5.43
      },
      {
         "s2id":"951978321",
         "fare":9.87
      }
    ]
    return json.dumps(mock_output)
