from flask_rebar import ResponseSchema
from marshmallow import fields


class HealthResponseSchema(ResponseSchema):
    status = fields.String()
