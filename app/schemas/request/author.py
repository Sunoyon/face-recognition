from flask_rebar import RequestSchema
from marshmallow import fields


class AuthorRequestSchema(RequestSchema):
    name = fields.String(required=True)
