"""
API Endpoints for Settings.
"""

from flask.views import MethodView
from flask_smorest import Blueprint
from marshmallow import fields, Schema


class SettingSchema(Schema):
    id = fields.Integer()


v1 = Blueprint(name="Settings", import_name=__name__, url_prefix="/api/v1/setting")


@v1.route("/")
class SettingView(MethodView):
    """
    API endpoints for settings.
    """

    @v1.response(201, SettingSchema(many=True))
    @v1.response(400, Schema())
    @v1.response(422, Schema())
    @v1.response(500, Schema())
    def get(self):
        """
        Get a list of settings.
        """
        return {"id": 0}

    @v1.response(201, SettingSchema())
    @v1.response(400, Schema())
    @v1.response(422, Schema())
    @v1.response(500, Schema())
    def post(self):
        """
        Create a new setting.
        """
        return {"id": 0}


@v1.route("/<setting_name>/")
class SettingByNameView(MethodView):
    """
    API endpoint to retrieve a setting.
    """

    @v1.response(200, SettingSchema(many=True))
    @v1.response(404, Schema())
    @v1.response(500, Schema())
    def get(self):
        """
        Get a setting.
        """
        return {"id": 0}

    @v1.response(200, SettingSchema(many=True))
    @v1.response(404, Schema())
    @v1.response(500, Schema())
    def patch(self):
        """
        Update attributes for a setting.
        """
        return {"id": 0}

    @v1.response(200, SettingSchema(many=True))
    @v1.response(404, Schema())
    @v1.response(500, Schema())
    def delete(self):
        """
        Delete a setting.
        """
        return {"id": 0}
