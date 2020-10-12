import base64
import json
import logging
import os
import unittest
from os.path import dirname

from app import create_app


class RecognizeTest(unittest.TestCase):

    def setUp(self) -> None:
        # To run with IDE
        base_dir = dirname(dirname(dirname(os.path.abspath(__file__))))
        os.chdir(base_dir)
        print("Changed to project directory: {}".format(base_dir))

        os.environ["APP_CONFIG"] = "config/test.cfg"
        self.app = create_app()
        self.client = self.app.test_client

        self.headers = {'content-type': 'application/json'}

        self.reference_file = "tests/images/sunoyon-2.jpg"
        self.unknown_file = "tests/images/sunoyon-1.jpg"
        self.detection_model = "hog"
        self.detection_upsample_cnt = 1
        self.landmark_model = "large"
        self.landmark_jitters_cnt = 10

    def tearDown(self) -> None:
        """teardown all initialized variables."""
        pass

    def test_recognize(self):
        with open(self.reference_file, "rb") as fp:
            img_data = fp.read()
            ref_base64 = base64.b64encode(img_data).decode("utf-8")
        with open(self.unknown_file, "rb") as fp:
            img_data = fp.read()
            unknown_base64 = base64.b64encode(img_data).decode("utf-8")
        recognize_request = {
            'refFaceImage': ref_base64,
            'unknownFaceImage': unknown_base64,
            'detectionModel': self.detection_model,
            'detectionUpsampleCount': self.detection_upsample_cnt,
            'landmarkModel': self.landmark_model,
            'landmarkJittersCount': 10
        }
        res = self.client().post('/v1/base/recognize', headers=self.headers, data=json.dumps(recognize_request))
        self.assertEqual(res.status_code, 200)
        response = json.loads(res.data.decode("utf-8"))
        logging.info("Response: %s", res.data.decode('utf-8'))
        self.assertEqual(response['matching'], True, "Face images mismatched")


if __name__ == '__main__':
    unittest.main()
