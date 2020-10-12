from flask_rebar import RequestSchema
from marshmallow import fields


class RecognitionRequestBase64Schema(RequestSchema):
    refFaceImage = fields.String(required=True)
    unknownFaceImage = fields.String(required=True)
    detectionUpsampleCount = fields.Integer(required=False, default=1)
    detectionModel = fields.String(required=False, default="hog")
    landmarkModel = fields.String(required=False, default="large")
    landmarkJittersCount = fields.Integer(required=False, default=10)

