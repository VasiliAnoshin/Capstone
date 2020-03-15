import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy
from app import create_app
from models import Movie, Actors, setup_db
import json
import pprint
from dotenv import load_dotenv
from pathlib import Path


class CapstoneTestCase(unittest.TestCase):
    def setUp(self):
        """Define test variables and initialize app."""
        env_path = Path('.') / 'setup.sh'
        load_dotenv(dotenv_path=env_path)
        self.app = create_app()
        self.client = self.app.test_client()
        self.database_name = "Capstone"
        self.database_path = os.getenv('DATABASE_URL')
        setup_db(self.app, self.database_path)

        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            self.db.create_all()

        def tearDown(self):
            """Executed after each test"""
            pass

    def test1_get_actors_without_token(self):
        res = self.client.get('/actors')
        self.assertEqual(res.status_code, 401)

    def test2_get_movies_without_token(self):
        res = self.client.get('/actors')
        self.assertEqual(res.status_code, 401)

    def test3_get_actors(self):
        res = self.client.get(
            '/actors',
            headers={
                "Authorization": f"Bearer {os.getenv('CASTING_DIRECTOR_JWT')}"
            }
        )
        self.assertEqual(res.status_code, 200)

    def test4_get_movies(self):
        if 'CASTING_DIRECTOR_JWT' in os.environ:
            res = self.client.get(
                '/movies',
                headers={
                    "Authorization": f"Bearer {
                        os.getenv('CASTING_DIRECTOR_JWT')}"
                }
            )
            self.assertEqual(res.status_code, 200)
        else:
            raise Exception(
                'Cat_Director was not provided in evironement variables')

    def test5_create_movies_without_permissions(self):
        res = self.client.post(
            '/movies/create',
            json={
                "title": "James Bond",
                "release_date": "2020-01-01"
            },
            headers={
                "Authorization": f"Bearer {os.getenv('CASTING_DIRECTOR_JWT')}"
            }
        )
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 401)

    def test13_create_actors(self):
        res = self.client.post(
            '/actors/create',
            json={
                "name": "Mikel Arteta",
                "gender": "male",
                "age": 43
            },
            headers={
                "Authorization": f"Bearer {
                    os.getenv('CASTING_DIRECTOR_JWT')}"
            }
        )
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'])

    def test6_create_actors(self):
        res = self.client.post(
            '/actors/create',
            json={
                "name": "Stiven Siegal",
                "gender": "male",
                "age": 51
            },
            headers={
                "Authorization": f"Bearer {os.getenv('CASTING_DIRECTOR_JWT')}"
            }
        )
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'])

    def test8_patch_actors(self):
        res = self.client.patch(
            '/actors/1',
            json={
                "name": "Brigit Bardo",
            },
            headers={
                "Authorization": f"Bearer {os.getenv('CASTING_DIRECTOR_JWT')}"
            }
        )
        self.assertEqual(res.status_code, 200)

    def test9_create_movie(self):
        res = self.client.post(
            '/movies/create',
            json={
                "title": "James Bond",
                "release_date": "2020-01-01"
            },
            headers={
                "Authorization": f"Bearer {
                    os.getenv('EXECUTIVE_PRODUCER_JWT')}"
            }
        )
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)

    def test10_patch_without_role_permission(self):
        res = self.client.patch(
            '/actors/1',
            json={
                "name": "Silvio Berluskoni"
            },
            headers={
                "Authorization": f"Bearer {os.getenv('CASTING_ASSISTANT_JWT')}"
            }
        )
        self.assertEqual(res.status_code, 401)

    def test12_delete_movie_without_delete_permissions(self):
        res = self.client.delete(
            '/movies/1',
            headers={
                "Authorization": f"Bearer {os.getenv('CASTING_DIRECTOR_JWT')}"
            }
        )
        self.assertEqual(res.status_code, 401)

    def test7_patch_actors_age(self):
        res = self.client.patch(
            '/actors/2',
            json={
                "age": 118,
            },
            headers={
                "Authorization": f"Bearer {os.getenv('CASTING_DIRECTOR_JWT')}"
            }
        )
        self.assertEqual(res.status_code, 200)

    def test_delete_actors(self):
        res = self.client.delete(
            '/actors/1',
            headers={
                "Authorization": f"Bearer {
                    os.getenv('EXECUTIVE_PRODUCER_JWT')}"
            }
        )
        self.assertEqual(res.status_code, 200)

# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
