"""
API Endpoints for Book Tags.
"""

from flask.views import MethodView
from flask_smorest import Blueprint
from marshmallow import fields, Schema


class BookTagSchema(Schema):
    id = fields.Integer()


v1 = Blueprint(name="Book Tags", import_name=__name__, url_prefix="/api/v1/book_tag")


@v1.route("/")
class BookTagView(MethodView):
    """
    API endpoints for book tags.
    """

    @v1.response(201, BookTagSchema(many=True))
    @v1.response(400, Schema())
    @v1.response(422, Schema())
    @v1.response(500, Schema())
    def get(self):
        """
        Get a list of book tags.
        """
        return {"id": 0}

    @v1.response(201, BookTagSchema())
    @v1.response(400, Schema())
    @v1.response(422, Schema())
    @v1.response(500, Schema())
    def post(self):
        """
        Create a new book tag.
        """
        return {"id": 0}


@v1.route("/<book_tag_id>/")
class BookTagByIdView(MethodView):
    """
    API endpoint to retrieve a book tag.
    """

    @v1.response(200, BookTagSchema(many=True))
    @v1.response(404, Schema())
    @v1.response(500, Schema())
    def get(self):
        """
        Get a book tag.
        """
        return {"id": 0}

    @v1.response(200, BookTagSchema(many=True))
    @v1.response(404, Schema())
    @v1.response(500, Schema())
    def patch(self):
        """
        Update attributes for a book tag.
        """
        return {"id": 0}

    @v1.response(200, BookTagSchema(many=True))
    @v1.response(404, Schema())
    @v1.response(500, Schema())
    def delete(self):
        """
        Delete a book tag.
        """
        return {"id": 0}
