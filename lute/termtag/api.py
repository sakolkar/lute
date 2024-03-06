"""
API Endpoints for Term Tags.
"""

from flask.views import MethodView
from flask_smorest import Blueprint
from marshmallow import fields, Schema


class TermTagSchema(Schema):
    id = fields.Integer()


v1 = Blueprint(name="Term Tags", import_name=__name__, url_prefix="/api/v1/term_tag")


@v1.route("/")
class TermTagView(MethodView):
    """
    API endpoints for term tags.
    """

    @v1.response(201, TermTagSchema(many=True))
    @v1.response(400, Schema())
    @v1.response(422, Schema())
    @v1.response(500, Schema())
    def get(self):
        """
        Get a list of term tags.
        """
        return {"id": 0}

    @v1.response(201, TermTagSchema())
    @v1.response(400, Schema())
    @v1.response(422, Schema())
    @v1.response(500, Schema())
    def post(self):
        """
        Create a new term tag.
        """
        return {"id": 0}


@v1.route("/<term_tag_id>/")
class TermTagByIdView(MethodView):
    """
    API endpoint to retrieve a term tag.
    """

    @v1.response(200, TermTagSchema(many=True))
    @v1.response(404, Schema())
    @v1.response(500, Schema())
    def get(self):
        """
        Get a term tag.
        """
        return {"id": 0}

    @v1.response(200, TermTagSchema(many=True))
    @v1.response(404, Schema())
    @v1.response(500, Schema())
    def patch(self):
        """
        Update attributes for a term tag.
        """
        return {"id": 0}

    @v1.response(200, TermTagSchema(many=True))
    @v1.response(404, Schema())
    @v1.response(500, Schema())
    def delete(self):
        """
        Delete a term tag.
        """
        return {"id": 0}
