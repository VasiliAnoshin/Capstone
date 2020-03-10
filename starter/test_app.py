import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy
from app import create_app
from models import Movie,Actors,setup_db
import json

Casting_Director_JWT = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ik5VUXdRa0l3UkVFM1JEWXlNalZGUVVRNFFrUkJOa1UwTXpVNE56azJOekJGTlVORE5ERTFSZyJ9.eyJpc3MiOiJodHRwczovL2ZzYmVuZnJhbmtsaW4uYXV0aDAuY29tLyIsInN1YiI6Imdvb2dsZS1vYXV0aDJ8MTA3OTQ1Mjg2NDA2MTkzOTU3MTE1IiwiYXVkIjpbIkNhcHN0b25lIiwiaHR0cHM6Ly9mc2JlbmZyYW5rbGluLmF1dGgwLmNvbS91c2VyaW5mbyJdLCJpYXQiOjE1ODM4NjkzNTMsImV4cCI6MTU4Mzk1NTc1MywiYXpwIjoibExhcEM1TFE1VW02ZnlHeExTOHF3RE9Cd1FSTXJnM1ciLCJzY29wZSI6Im9wZW5pZCBwcm9maWxlIGVtYWlsIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmFjdG9yIiwiZ2V0OmFjdG9ycyIsImdldDptb3ZpZXMiLCJwYXRjaDphY3RvciIsInBhdGNoOm1vdmllIiwicG9zdDphY3RvcnMiXX0.Habzpqq8etWWaaWW76cc8sBtS881QYWcj7qJSlmVYCqfCfY6hS1qgn4_lZGy4O3zeMTM9QKlbdcrYwSi8eJ9cHG62-p75wdyRRyN7ZTRdZJYN1IgtlF3Bm4Pzt3g7cAPATNgLNZwAWs0_j1ZB0G-JIDmpiEddP_SPpyTNmNcNVxjJkBTjvhD3tQKIEXJpD-QNJxVFctHRPpg5_imP0XGoFTgMQ37_jNhtSsntM1qo0E1RnGA-40myq7IVnvDaXAzG3nZ70zsjU303cA-fNr9plla8PnNIVpsHC3GQVxw6UykV37-k7iHoaTC5rS_TiJSIb_XvtqlsVMKn_lETHnPjA"
Executive_Producer_JWT = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ik5VUXdRa0l3UkVFM1JEWXlNalZGUVVRNFFrUkJOa1UwTXpVNE56azJOekJGTlVORE5ERTFSZyJ9.eyJpc3MiOiJodHRwczovL2ZzYmVuZnJhbmtsaW4uYXV0aDAuY29tLyIsInN1YiI6Imdvb2dsZS1vYXV0aDJ8MTA3OTQ1Mjg2NDA2MTkzOTU3MTE1IiwiYXVkIjpbIkNhcHN0b25lIiwiaHR0cHM6Ly9mc2JlbmZyYW5rbGluLmF1dGgwLmNvbS91c2VyaW5mbyJdLCJpYXQiOjE1ODM4Njk5MTEsImV4cCI6MTU4Mzk1NjMxMSwiYXpwIjoibExhcEM1TFE1VW02ZnlHeExTOHF3RE9Cd1FSTXJnM1ciLCJzY29wZSI6Im9wZW5pZCBwcm9maWxlIGVtYWlsIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmFjdG9yIiwiZGVsZXRlOm1vdmllIiwiZ2V0OmFjdG9ycyIsImdldDptb3ZpZXMiLCJwYXRjaDphY3RvciIsInBhdGNoOm1vdmllIiwicG9zdDphY3RvcnMiLCJwb3N0Om1vdmllcyJdfQ.Ta8W-WD97lusKiJMpQnhLGB-XH23tZtclvTBHaddQgx2wLk1s9OQRLCcXjL3EHPnzWj4NVuP4du6NSszSGsIYXCyBJzGYQptukofKpYMU3Z3DYPUv_xSREUDGV_ro8nIfkOzkpdc32ztmDo1Ii_7mLmMqk2YIkLj-dO_v5nxglitGqqUj_pV7d2tkCsHI4YtCVH_cWNAn13x8jt0LLbWGFfsCxUcYfJg4umOaVap1eozyM8cxupT52fWZy0soKWC0sq-kBnGuTCxiN42-WzkXENqRgk7XOZBtoRQdZ424QlwMvCDdw45DkwoExDN9pKaPCE1xDWrWCq4I6kKmx97lg"
Casting_Assistant_JWT = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ik5VUXdRa0l3UkVFM1JEWXlNalZGUVVRNFFrUkJOa1UwTXpVNE56azJOekJGTlVORE5ERTFSZyJ9.eyJpc3MiOiJodHRwczovL2ZzYmVuZnJhbmtsaW4uYXV0aDAuY29tLyIsInN1YiI6Imdvb2dsZS1vYXV0aDJ8MTA3OTQ1Mjg2NDA2MTkzOTU3MTE1IiwiYXVkIjpbIkNhcHN0b25lIiwiaHR0cHM6Ly9mc2JlbmZyYW5rbGluLmF1dGgwLmNvbS91c2VyaW5mbyJdLCJpYXQiOjE1ODM4Nzg2MjUsImV4cCI6MTU4Mzk2NTAyNSwiYXpwIjoibExhcEM1TFE1VW02ZnlHeExTOHF3RE9Cd1FSTXJnM1ciLCJzY29wZSI6Im9wZW5pZCBwcm9maWxlIGVtYWlsIiwicGVybWlzc2lvbnMiOlsiZ2V0OmFjdG9ycyIsImdldDptb3ZpZXMiXX0.TB4OLMwt28LbTBpsap4w1UwcJLkY14KC8e4CcHmMddSbZMdqshczMA2Zz-oTL8823DPtB15q8fh2lt5Ma56TIwXkXFwMoENetGRhLCjkIzhFPqKu7JuqDrp_NTVlYocCs16n6qwkyVESQL6T6YMGCt733h3XqQ08y-OQR8_sP1FgL6BfySU_2CnW5cLFASAcRLYuIadvdh30fKN723uMa74WGMoZddDa45N-dVXyxzCfRiAZetaBr58ATs_qSOtFZeMvtWRQ6op8VWmz9VVI7nqnWJzHgF4b1h6QqvwC213eATURDe5p4HazAOqznVZtwV-vjonGLrINchlOOofHBw"

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

    def test_create_actors(self):
        res = self.client.post(
            '/actors/create',
            json={
                "name": "Stiven Siegal",
                "gender": "male",
                "age": 51
            },
            headers={
                "Authorization": f"Bearer {Casting_Director_JWT}"
            }
        )
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)

    def test_patch_actors_age(self):
        res = self.client.patch(
            '/actors/1',
            json={
                "age": "18"
            },
            headers={
                "Authorization": f"Bearer {Casting_Director_JWT}"
            }
        )
        self.assertEqual(res.status_code, 200)

    def test_patch_actors(self):
        res = self.client.patch(
            '/actors/1',
            json={
                "name": "Brigit Bardo"
            },
            headers={
                "Authorization": f"Bearer {Casting_Director_JWT}"
            }
        )
        self.assertEqual(res.status_code, 200)

    def test_delete_movie_without_delete_permissions(self):
        res = self.client.delete(
            '/movies/1',
            headers={
                "Authorization": f"Bearer {Casting_Director_JWT}"
            }
        )
        self.assertEqual(res.status_code, 401)

    def test_delete_actors(self):
        res = self.client.delete(
            '/actors/1',
            headers={
                "Authorization": f"Bearer {Casting_Director_JWT}"
            }
        )
        self.assertEqual(res.status_code, 200)
    
    def test_create_movie(self):
        res = self.client.post(
            '/movies/create',
            json={
                "title": "James Bond",
                "release_date": "2020-01-01"
            },
            headers={
                "Authorization": f"Bearer {Executive_Producer_JWT}"
            }
        )
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
    
    def test_patch_without_role_permission(self):
        res = self.client.patch(
            '/actors/1',
            json={
                "name": "Brigit Bardo"
            },
            headers={
                "Authorization": f"Bearer {Casting_Assistant_JWT}"
            }
        )
        self.assertEqual(res.status_code, 401)

    def test_delete_movie_with_role_permission(self):
        res = self.client.delete(
            '/movies/1',
            headers={
                "Authorization": f"Bearer {Executive_Producer_JWT}"
            }
        )
        self.assertEqual(res.status_code, 200)

# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()