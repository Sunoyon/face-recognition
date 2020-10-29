import logging

import flask_rebar
from flask import current_app

from app.app import v1_registry
from app.schemas.request.recognition import RecognitionRequestBase64Schema
from app.schemas.response.recognition import BaseFaceRecognitionResponseSchema
from app.services import recognition


@v1_registry.handles(
    rule="/base/recognize",
    method="POST",
    mimetype="application/json",
    request_body_schema=RecognitionRequestBase64Schema(),
    response_body_schema={200: BaseFaceRecognitionResponseSchema}
)
def recognize():
    """
    Face Recognition REST API

    Parameters:
        refFaceImage (string):           Base64 string data of reference image (or, first image)
        unknownFaceImage (string):       Base64 string data of unknown image (or, second image)
        detectionModel (string):         Model name for face detection. Expected values: hog, cnn. Default: hog
        landmarkModel (string):          Model name for landmark detection. Expected values: large, small. Default: large
        detectionUpsampleCount (int):    Detection up-sample count. Default: 1
        landmarkJittersCount (int):      Landmark jitter count. Default: 10

    Returns:
        matching (boolean):              The two faces match or not.
        distance (float):                Distance of the two faces. (0-1)
    """
    body = flask_rebar.get_validated_body()
    logging.info("Detection Model: %s, Landmark Model: %s", body['detectionModel'], body['landmarkModel'])
    tolerance = current_app.config['FACE_RECOGNITION_DLIB_DISTANCE_TOLERANCE']
    face_distance = recognition.distance(reference_image=body['refFaceImage'],
                                         unknown_image=body['unknownFaceImage'],
                                         image_format="base64",
                                         detection_number_of_times_to_upsample=body['detectionUpsampleCount'],
                                         detection_model=body['detectionModel'],
                                         num_jitters=body['landmarkJittersCount'],
                                         landmark_model=body['landmarkModel'])
    distance = BaseFaceRecognitionResponseSchema()
    distance.distance = face_distance
    distance.matching = face_distance < tolerance
    return distance, 200
