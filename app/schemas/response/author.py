from marshmallow import fields
from flask_rebar import ResponseSchema


class AuthorResponseSchema(ResponseSchema):
    id = fields.Integer()
    name = fields.String()
    created_at = fields.DateTime("%Y-%m-%d %H:%M:%S")
    updated_at = fields.DateTime("%Y-%m-%d %H:%M:%S")
