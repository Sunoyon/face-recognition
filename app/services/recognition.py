import base64
import logging
from io import BytesIO

import face_recognition
import numpy as np
from face_recognition.api import _css_to_rect, \
    pose_predictor_68_point, pose_predictor_5_point, face_encoder

from app.exceptions.errors import AppError


def load(image, image_format='file'):
    if image_format == 'file':
        img = face_recognition.load_image_file(image)
        return img
    elif image_format == 'base64':
        file = BytesIO(base64.b64decode(image))
        return face_recognition.load_image_file(file)
    else:
        logging.error("Invalid face image format. [image_format= %s]", image_format)
        raise AppError(status_code=406, message="Invalid face image format")


def face_locations(image, number_of_times_to_upsample, model):
    return face_recognition.face_locations(img=image, number_of_times_to_upsample=number_of_times_to_upsample,
                                           model=model)


def raw_face_landmarks(face_image, face_locs, model):
    face_locs = [_css_to_rect(face_location) for face_location in face_locs]
    pose_predictor = pose_predictor_68_point

    if model == "small":
        pose_predictor = pose_predictor_5_point

    return [pose_predictor(face_image, face_location) for face_location in face_locs]


def face_encodings(face_image, raw_landmarks, num_jitters):
    return [np.array(face_encoder.compute_face_descriptor(face_image, raw_landmark_set, num_jitters))
            for raw_landmark_set in raw_landmarks]


def distance(
        reference_image, unknown_image, image_format,
        detection_number_of_times_to_upsample, detection_model,
        landmark_model, num_jitters):
    # Load images
    reference = load(reference_image, image_format)
    unknown = load(unknown_image, image_format)

    # Face detections
    ref_face_locations = face_locations(image=reference,
                                        number_of_times_to_upsample=detection_number_of_times_to_upsample,
                                        model=detection_model)
    unknown_face_locations = face_locations(image=unknown,
                                            number_of_times_to_upsample=detection_number_of_times_to_upsample,
                                            model=detection_model)

    # Face landmarks
    ref_face_landmarks = raw_face_landmarks(face_image=reference,
                                            face_locs=ref_face_locations,
                                            model=landmark_model)
    unknown_face_landmarks = raw_face_landmarks(face_image=unknown,
                                                face_locs=unknown_face_locations,
                                                model=landmark_model)
    # Face encoding
    ref_face_encoding = face_encodings(face_image=reference,
                                       raw_landmarks=ref_face_landmarks,
                                       num_jitters=num_jitters)
    unknown_face_encoding = face_encodings(face_image=unknown,
                                           raw_landmarks=unknown_face_landmarks,
                                           num_jitters=num_jitters)

    # Check only single face is available
    if len(ref_face_encoding) != 1:
        logging.error("No face or more than 1 face found in reference image. Face count [%d]",
                      len(ref_face_encoding))
        raise AppError(status_code=406, message="No face or more than 1 face found in reference image.")
    if len(unknown_face_encoding) != 1:
        logging.error("No face or more than 1 face found in unknown image. Face count [%d]",
                      len(unknown_face_encoding))
        raise AppError(status_code=406, message="No face or more than 1 face found in unknown image.")

    distance = face_recognition.face_distance([ref_face_encoding[0]], unknown_face_encoding[0])
    logging.info("distance of two faces: %f", distance[0])
    return distance[0]
