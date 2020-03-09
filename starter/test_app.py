import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy
from app import create_app
from models import Movie,Actors,setup_db
import json

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
        
# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()