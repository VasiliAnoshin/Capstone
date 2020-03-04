import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_migrate import Migrate
from init import create_app
from models import *

#----------------------------------------------------------------------------#
# App Config.
#----------------------------------------------------------------------------#
app = create_app()
migrate = Migrate(app,db)

def format_data(data):
  return [d.format() for d in data]

#  Movies
#  ----------------------------------------------------------------
@app.route('/movies')
def get_movies():
  query = Movie.query.all()

  return jsonify({
            'movies': format_data(query),
            'success': True
  })

#  Actors
#  ----------------------------------------------------------------
@app.route('/actors')
def get_actors():
  query = Actors.query.all()

  return jsonify({
            'actors': format_data(query),
            'success': True
  })


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)