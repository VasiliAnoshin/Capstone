import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_migrate import Migrate
from init import create_app
from models import *
import sys

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

@app.route('/movies/create', methods=['POST'])
def create_movie():
  try:
    req=request.get_json()
    movie = Movie(title=req['title'], release_date=req['release_date'])
    db.session.add(movie)
    db.session.commit()
    return jsonify({
          "success":True
      })
  except:
    print(sys.exc_info())
    db.session.rollback()
    abort(404)

@app.route('/movies/<int:id>', methods=['DELETE'])
def delete_movie(id):
    try:
      movie = Movie.query.filter(Movie.id==id).one_or_none()
      db.session.delete(movie)
      db.session.commit()
      return jsonify({
          'success':True
      })
    except:
      abort(404)

@app.route('/movies/<int:id>', methods=['PATCH'])
def update_movie(id):
  try:
   req = request.get_json()
   movie = Movie.query.filter(Movie.id==id).one_or_none()
   if('title' in req):
    movie.title = req['title']
   if('release_date' in req):
    movie.release_date = req['release_date']
    
   db.session.commit()
   return jsonify({
      'success':True
    })
  except:
    abort(404)

#  Actors
#  ----------------------------------------------------------------
@app.route('/actors')
def get_actors():
  query=Actors.query.all()
  
  return jsonify({
            'actors': format_data(query),
            'success': True
  })

@app.route('/actors/create', methods=['POST'])
def create_actors():
  try:
    req=request.get_json()
    actor = Actors(name=req['name'], gender=req['gender'],age=req['age'])
    db.session.add(actor)
    db.session.commit()
    return jsonify({
          "success":True
      })
  except:
    db.session.rollback()
    abort(404)

@app.route('/actors/<int:id>', methods=['DELETE'])
def delete_actor(id):
    try:
      actor = Actors.query.filter(Actors.id==id).one_or_none()
      db.session.delete(actor)
      db.session.commit()
      return jsonify({
          'success':True
      })
    except:
      abort(404)

@app.route('/actors/<int:id>', methods=['PATCH'])
def update_actor(id):
  try:
   req = request.get_json()
   actor = Actors.query.filter(Actors.id==id).one_or_none()
   if('name' in req):
    actor.name = req['name']
   if('gender' in req):
    actor.gender = req['gender']
   if('age' in req):
    actor.age = req['age']
    
   db.session.commit()
   return jsonify({
      'success':True
    })
  except:
    abort(404)

#  Error Wrappers
#  ----------------------------------------------------------------
@app.errorhandler(404)
def not_found(error):
    return jsonify({
      "success": False,
      "error": 404,
      "message":"resourse not found"
  }), 404

@app.errorhandler(422)
def unprocessable(error):
    return jsonify({
      "success": False,
      "error": 422,
      "message":"unprocessable"
  }), 422

@app.errorhandler(405)
def method_not_allowed(error):
    return jsonify({
      'code': 405,
      'success': False,
      'message': 'method not allowed'
  }), 405

@app.errorhandler(500)
def internal_server_error(error):
    return jsonify({
      'code': 500,
      'success': False,
      'message': 'server error'
  }), 500  

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)