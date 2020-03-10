import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy
from app import create_app
from models import Movie,Actors,setup_db
import json

Casting_Director_JWT = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ik5VUXdRa0l3UkVFM1JEWXlNalZGUVVRNFFrUkJOa1UwTXpVNE56azJOekJGTlVORE5ERTFSZyJ9.eyJpc3MiOiJodHRwczovL2ZzYmVuZnJhbmtsaW4uYXV0aDAuY29tLyIsInN1YiI6Imdvb2dsZS1vYXV0aDJ8MTA3OTQ1Mjg2NDA2MTkzOTU3MTE1IiwiYXVkIjpbIkNhcHN0b25lIiwiaHR0cHM6Ly9mc2JlbmZyYW5rbGluLmF1dGgwLmNvbS91c2VyaW5mbyJdLCJpYXQiOjE1ODM4MjQ4ODQsImV4cCI6MTU4MzkxMTI4NCwiYXpwIjoibExhcEM1TFE1VW02ZnlHeExTOHF3RE9Cd1FSTXJnM1ciLCJzY29wZSI6Im9wZW5pZCBwcm9maWxlIGVtYWlsIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmFjdG9yIiwiZ2V0OmFjdG9ycyIsImdldDptb3ZpZXMiLCJwYXRjaDphY3RvciIsInBhdGNoOm1vdmllIiwicG9zdDphY3RvcnMiXX0.Fx4K6AqHR9ZyphVd5zcWzLH3khCAjT8Peiqg4T0LumJftqVo0F2ZCyQDQhVBIOKrRsklOpU0KtQ0blBE4GQ2HU_L0ifqvvbsT2TS7lcqmmgi-IfUz1-wHseRit_2mz3X7H_2Rm6bmYrHEgYYK3DSVqZVMMpCR7_AdF2X7zPyivukDe1lRmpc4Ka2SWRrJJanvVWCjrI3D-lJWfcyoMxwJ55rA-K10puTZJJdJCliicOoaGbbRJcCt9k6SnNdvyXXACYPmFXxiLRvErOJCmGFylUq7VAK5kYBaYDjLtYWjTCJLJB4Eou-XNnkE2Gt8NUdoKFafLram4w2rilEK0mAsA"

class CapstoneTestCase(unittest.TestCase):
    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client()
        self.database_name = "Capstone"
        self.database_path = "postgresql://{}/{}".format('localhost:5432', self.database_name)
        setup_db(self.app, self.database_path)

        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            self.db.create_all()
        
        def tearDown(self):
            """Executed after each test"""
            pass
    
    def test_get_actors_without_token(self):
        res = self.client.get('/actors')
        self.assertEqual(res.status_code, 401)
    
    def test_get_movies_without_token(self):
        res = self.client.get('/actors')
        self.assertEqual(res.status_code, 401)
    
    def test_get_actors(self):
        res = self.client.get(
            '/actors',
            headers={
                "Authorization": f"Bearer {Casting_Director_JWT}"
            }
        )
        self.assertEqual(res.status_code, 200)
    
    def test_get_movies(self):
        res = self.client.get(
            '/movies',
            headers={
                "Authorization": f"Bearer {Casting_Director_JWT}"
            }
        )
        self.assertEqual(res.status_code, 200)
    
    def test_create_movies_without_permissions(self):
        res = self.client.post(
            '/movies/create',
            json={
                "title": "James Bond",
                "release_date": "2020-01-01"
            },
            headers={
                "Authorization": f"Bearer {Casting_Director_JWT}"
            }
        )
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 401)

    
        
# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()