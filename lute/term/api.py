"""
API Endpoints for Terms.
"""

from flask.views import MethodView
from flask_smorest import Blueprint
from marshmallow import fields, Schema


class TermSchema(Schema):
    id = fields.Integer()


v1 = Blueprint(name="Terms", import_name=__name__, url_prefix="/api/v1/term")


@v1.route("/<term_id>/")
class TermView(MethodView):
    """
    API endpoints for terms.
    """

    @v1.response(201, TermSchema(many=True))
    @v1.response(400, Schema())
    @v1.response(422, Schema())
    @v1.response(500, Schema())
    def get(self):
        """
        Get a term by id.
        """
        return {"id": 0}

    @v1.response(201, TermSchema(many=True))
    @v1.response(400, Schema())
    @v1.response(422, Schema())
    @v1.response(500, Schema())
    def patch(self):
        """
        Update a term.
        """
        return {"id": 0}

    @v1.response(201, TermSchema(many=True))
    @v1.response(400, Schema())
    @v1.response(422, Schema())
    @v1.response(500, Schema())
    def delete(self):
        """
        Delete a term.
        """
        return {"id": 0}
