"""
API Endpoints for Backups.
"""

from flask.views import MethodView
from flask_smorest import Blueprint
from marshmallow import fields, Schema


class BackupSchema(Schema):
    id = fields.Integer()


v1 = Blueprint(name="Backups", import_name=__name__, url_prefix="/api/v1/backup")


@v1.route("/")
class BackupView(MethodView):
    """
    API endpoints for backups in general.
    """

    @v1.response(200, BackupSchema(many=True))
    @v1.response(404, Schema())
    @v1.response(500, Schema())
    def get(self):
        """
        Return a list of all backups.
        """
        return {"id": 0}

    @v1.response(201, BackupSchema())
    @v1.response(400, Schema())
    @v1.response(422, Schema())
    @v1.response(500, Schema())
    def post(self):
        """
        Create a new backup.
        """
        return {"id": 0}


@v1.route("/<name>/")
class BackupByIdView(MethodView):
    """
    API endpoints for a specific backup.
    """

    @v1.response(200, BackupSchema(many=True))
    @v1.response(404, Schema())
    @v1.response(500, Schema())
    def get(self):
        """
        Get details for a specific backup.
        """
        return {"id": 0}

    @v1.response(200, BackupSchema())
    @v1.response(404, Schema())
    @v1.response(500, Schema())
    def patch(self):
        """
        Update attributes of a specific backup.
        """
        return {"id": 0}

    @v1.response(200, BackupSchema())
    @v1.response(404, Schema())
    @v1.response(500, Schema())
    def delete(self):
        """
        Delete a specific backup.
        """
        return {"id": 0}


@v1.route("/<name>/download")
class BackupByIdDownloadView(MethodView):
    """
    API endpoint to retrieve the content of a backup.
    """

    @v1.response(200, BackupSchema(many=True))
    @v1.response(404, Schema())
    @v1.response(500, Schema())
    def get(self):
        """
        Get the contents of a backup.
        """
        return {"id": 0}
