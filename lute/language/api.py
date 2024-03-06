"""
API Endpoints for Languages.
"""

from flask.views import MethodView
from flask_smorest import Blueprint
from marshmallow import fields, Schema


class LanguageSchema(Schema):
    id = fields.Integer()


v1 = Blueprint(name="Languages", import_name=__name__, url_prefix="/api/v1/language")


@v1.route("/")
class LanguageView(MethodView):
    """
    API endpoints for languages.
    """

    @v1.response(201, LanguageSchema(many=True))
    @v1.response(400, Schema())
    @v1.response(422, Schema())
    @v1.response(500, Schema())
    def get(self):
        """
        Get a list of languages.
        """
        return {"id": 0}

    @v1.response(201, LanguageSchema())
    @v1.response(400, Schema())
    @v1.response(422, Schema())
    @v1.response(500, Schema())
    def post(self):
        """
        Create a new language.
        """
        return {"id": 0}


@v1.route("/<language_id>/")
class LanguageByIdView(MethodView):
    """
    API endpoint to retrieve a language.
    """

    @v1.response(200, LanguageSchema(many=True))
    @v1.response(404, Schema())
    @v1.response(500, Schema())
    def get(self):
        """
        Get a language.
        """
        return {"id": 0}

    @v1.response(200, LanguageSchema(many=True))
    @v1.response(404, Schema())
    @v1.response(500, Schema())
    def patch(self):
        """
        Update attributes for a language.
        """
        return {"id": 0}

    @v1.response(200, LanguageSchema(many=True))
    @v1.response(404, Schema())
    @v1.response(500, Schema())
    def delete(self):
        """
        Delete a language.
        """
        return {"id": 0}


@v1.route("/<language_id>/<term_text>/")
class LanguageTermView(MethodView):
    """
    API endpoint to manage terms by text for a language.
    """

    @v1.response(200, LanguageSchema(many=True))
    @v1.response(404, Schema())
    @v1.response(500, Schema())
    def get(self):
        """
        Get an term by text.
        """
        return {"id": 0}

    @v1.response(200, LanguageSchema(many=True))
    @v1.response(404, Schema())
    @v1.response(500, Schema())
    def post(self):
        """
        Create a term by text.
        """
        return {"id": 0}


@v1.route("/<language_id>/<term_text>/parent/")
class LanguageTermParentView(MethodView):
    """
    API endpoint to search for parents by text for a language.
    """

    @v1.response(200, LanguageSchema(many=True))
    @v1.response(404, Schema())
    @v1.response(500, Schema())
    def get(self):
        """
        Get a list of possible parent terms by text.
        """
        return {"id": 0}


@v1.route("/<language_id>/<term_text>/sentence/")
class LanguageTermSentenceView(MethodView):
    """
    API endpoint to search for sentences by text for a language.
    """

    @v1.response(200, LanguageSchema(many=True))
    @v1.response(404, Schema())
    @v1.response(500, Schema())
    def get(self):
        """
        Get a list of sentences by text.
        """
        return {"id": 0}


@v1.route("/<language_id>/<term_text>/image/")
class ImageByTermView(MethodView):
    """
    API endpoint to retrieve an image.
    """

    @v1.response(200, LanguageSchema(many=True))
    @v1.response(404, Schema())
    @v1.response(500, Schema())
    def get(self):
        """
        Get an image for a term.
        """
        return {"id": 0}

    @v1.response(200, LanguageSchema(many=True))
    @v1.response(404, Schema())
    @v1.response(500, Schema())
    def post(self):
        """
        Create an image for a term.
        """
        return {"id": 0}

    @v1.response(200, LanguageSchema(many=True))
    @v1.response(404, Schema())
    @v1.response(500, Schema())
    def patch(self):
        """
        Update the image for a term.
        """
        return {"id": 0}

    @v1.response(200, LanguageSchema(many=True))
    @v1.response(404, Schema())
    @v1.response(500, Schema())
    def delete(self):
        """
        Delete the image for a term.
        """
        return {"id": 0}
