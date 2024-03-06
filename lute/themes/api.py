"""
API Endpoints for Themes.
"""

from flask.views import MethodView
from flask_smorest import Blueprint
from marshmallow import fields, Schema


class ThemeSchema(Schema):
    id = fields.Integer()


v1 = Blueprint(name="Themes", import_name=__name__, url_prefix="/api/v1/theme")


@v1.route("/")
class ThemeView(MethodView):
    """
    API endpoints for themes.
    """

    @v1.response(201, ThemeSchema(many=True))
    @v1.response(400, Schema())
    @v1.response(422, Schema())
    @v1.response(500, Schema())
    def get(self):
        """
        Get a list of themes.
        """
        return {"id": 0}
