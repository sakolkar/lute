"""
API Endpoints for Books.
"""

from flask.views import MethodView
from flask_smorest import Blueprint
from marshmallow import fields, Schema


class BookSchema(Schema):
    id = fields.Integer()


v1 = Blueprint(name="Books", import_name=__name__, url_prefix="/api/v1/book")


@v1.route("/")
class BookView(MethodView):
    """
    API endpoints for books.
    """

    @v1.response(201, BookSchema(many=True))
    @v1.response(400, Schema())
    @v1.response(422, Schema())
    @v1.response(500, Schema())
    def get(self):
        """
        Get a list of books.
        """
        return {"id": 0}

    @v1.response(201, BookSchema())
    @v1.response(400, Schema())
    @v1.response(422, Schema())
    @v1.response(500, Schema())
    def post(self):
        """
        Create a new book.
        """
        return {"id": 0}


@v1.route("/<book_id>/")
class BookByIdView(MethodView):
    """
    API endpoints to retrieve a book.
    """

    @v1.response(200, BookSchema())
    @v1.response(404, Schema())
    @v1.response(500, Schema())
    def get(self):
        """
        Get a book.
        """
        return {"id": 0}

    @v1.response(200, BookSchema())
    @v1.response(404, Schema())
    @v1.response(500, Schema())
    def patch(self):
        """
        Update attributes for a book.
        """
        return {"id": 0}

    @v1.response(200, BookSchema())
    @v1.response(404, Schema())
    @v1.response(500, Schema())
    def delete(self):
        """
        Delete a book.
        """
        return {"id": 0}


@v1.route("/<book_id>/audio/")
class BookAudioView(MethodView):
    """
    API endpoints for book audio.
    """

    @v1.response(200, BookSchema())
    @v1.response(404, Schema())
    @v1.response(500, Schema())
    def get(self):
        """
        Get the audio from a book.
        """
        return {"id": 0}

    @v1.response(201, BookSchema())
    @v1.response(400, Schema())
    @v1.response(422, Schema())
    @v1.response(500, Schema())
    def post(self):
        """
        Set the audio for a book.
        """
        return {"id": 0}

    @v1.response(200, BookSchema())
    @v1.response(404, Schema())
    @v1.response(500, Schema())
    def patch(self):
        """
        Update attributes for the audio for a book.
        """
        return {"id": 0}

    @v1.response(200, BookSchema())
    @v1.response(404, Schema())
    @v1.response(500, Schema())
    def delete(self):
        """
        Delete the audio for a book.
        """
        return {"id": 0}


@v1.route("/<book_id>/audio/stream")
class BookAudioStreamView(MethodView):
    """
    API endpoint to stream book audio.
    """

    @v1.response(200, BookSchema())
    @v1.response(404, Schema())
    @v1.response(500, Schema())
    def get(self):
        """
        Get the audio stream for a book.
        """
        return {"id": 0}


@v1.route("/<book_id>/page/<page_num>/")
class PageByIdView(MethodView):
    """
    API endpoints for book pages.
    """

    @v1.response(200, BookSchema())
    @v1.response(404, Schema())
    @v1.response(500, Schema())
    def get(self):
        """
        Get a page from a book.
        """
        return {"id": 0}

    @v1.response(200, BookSchema())
    @v1.response(404, Schema())
    @v1.response(500, Schema())
    def patch(self):
        """
        Update attributes for a page in a book.
        """
        return {"id": 0}
