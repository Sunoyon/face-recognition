from flask_rebar import ResponseSchema
from marshmallow import fields

from app.schemas.response.author import AuthorResponseSchema


class BookResponseSchema(ResponseSchema):
    id = fields.Integer()
    title = fields.String()
    description = fields.String()
    created_at = fields.DateTime("%Y-%m-%d %H:%M:%S")
    updated_at = fields.DateTime("%Y-%m-%d %H:%M:%S")
    author = fields.Nested(AuthorResponseSchema)
