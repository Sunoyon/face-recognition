import base64
import os
import unittest
from os.path import dirname

from app.services.recognition import distance, load, face_locations, raw_face_landmarks


class RecognitionTest(unittest.TestCase):

    def setUp(self) -> None:
        base_dir = dirname(dirname(dirname(os.path.abspath(__file__))))
        os.chdir(base_dir)
        print("Changed to project directory: {}".format(base_dir))

        self.reference_file = "tests/images/sunoyon-2.jpg"
        self.unknown_file = "tests/images/sunoyon-1.jpg"
        self.image_format = "file"

    def tearDown(self) -> None:
        pass

    def test_face_recognition(self):
        result = distance(reference_image=self.reference_file,
                          unknown_image=self.unknown_file,
                          image_format=self.image_format,
                          detection_number_of_times_to_upsample=1,
                          detection_model="hog",
                          landmark_model="large",
                          num_jitters=10)
        print("Distance of test pictures: {}".format(result))

        with open(self.reference_file, "rb") as fp:
            img_data = fp.read()
            ref_base64 = base64.b64encode(img_data)
        with open(self.unknown_file, "rb") as fp:
            img_data = fp.read()
            unknown_base64 = base64.b64encode(img_data)

        result = distance(reference_image=ref_base64,
                          unknown_image=unknown_base64,
                          image_format="base64",
                          detection_number_of_times_to_upsample=1,
                          detection_model="hog",
                          landmark_model="large",
                          num_jitters=10)
        print("Distance of test pictures using base64: {}".format(result))

    def test_load(self):
        img_numpy_array = load(image=self.reference_file, image_format=self.image_format)
        print(img_numpy_array)

    def test_raw_face_locations(self):
        img_numpy_array = load(image=self.reference_file, image_format=self.image_format)
        face_locations_hog = face_locations(image=img_numpy_array, number_of_times_to_upsample=1, model="hog")
        print("Face location using hog")
        print(face_locations_hog)

        # face_locations_cnn = raw_face_locations(image=img_numpy_array, number_of_times_to_upsample=1, model="cnn")
        # print("Face location using cnn")
        # print(face_locations_cnn)

    def test_raw_face_landmarks(self):
        img_numpy_array = load(image=self.reference_file, image_format=self.image_format)
        face_locations_hog = face_locations(image=img_numpy_array, number_of_times_to_upsample=1,
                                            model="hog")
        landmarks = raw_face_landmarks(face_image=img_numpy_array, face_locs=face_locations_hog, model="large")
        print(landmarks)


if __name__ == '__main__':
    unittest.main()
