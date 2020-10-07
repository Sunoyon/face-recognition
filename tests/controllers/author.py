import unittest
import os
import json

from app import create_app
from app.app import db


class AuthorTest(unittest.TestCase):
    """This class represents the author tests case"""

    def setUp(self) -> None:
        os.environ["APP_CONFIG"] = "config/tests.cfg"
        self.app = create_app()
        self.client = self.app.test_client
        self.author = {'name': 'Rabindranath Tagore'}
        self.headers = {'content-type': 'application/json'}

        with self.app.app_context():
            db.create_all()

    def tearDown(self) -> None:
        """teardown all initialized variables."""
        with self.app.app_context():
            # drop all tables
            db.session.remove()
            db.drop_all()

    def test_create_author(self):
        """Test API can create a author (POST request)"""
        res = self.client().post('/v1/author', headers=self.headers, json=self.author)
        self.assertEqual(res.status_code, 201)
        response_author = json.loads(res.data.decode("utf-8"))
        self.assertIn(self.author['name'], response_author['name'], "Author name mismatched")
