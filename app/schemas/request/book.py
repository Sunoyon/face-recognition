from flask_rebar import RequestSchema
from marshmallow import fields


class BookRequestSchema(RequestSchema):
    title = fields.String(required=True)
    description = fields.String(required=False)
    author_id = fields.Integer(required=True)
