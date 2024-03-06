"""
API Endpoints for Stats.
"""

from flask.views import MethodView
from flask_smorest import Blueprint
from marshmallow import fields, Schema


class StatisticSchema(Schema):
    id = fields.Integer()


v1 = Blueprint(name="Statistics", import_name=__name__, url_prefix="/api/v1/statistic")


@v1.route("/")
class StatisticView(MethodView):
    """
    API endpoints for statistics.
    """

    @v1.response(201, StatisticSchema(many=True))
    @v1.response(400, Schema())
    @v1.response(422, Schema())
    @v1.response(500, Schema())
    def get(self):
        """
        Get a list of statistics.
        """
        return {"id": 0}
