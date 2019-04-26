"""Returns fare
"""

from flask import (
    Blueprint,
    current_app,
    jsonify
)

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

    date = args["date"]   # noqa: F841
    records = (current_app.fare["heatmap"]
               .query('date == @date')
               .loc[:, ["si2d", "total_amount"]])
    return jsonify(records.to_dict(orient='records'))
