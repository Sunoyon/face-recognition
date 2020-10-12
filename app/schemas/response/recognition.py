from flask_rebar import ResponseSchema
from marshmallow import fields


class BaseFaceRecognitionResponseSchema(ResponseSchema):
    distance = fields.Float()
    matching = fields.Boolean()
