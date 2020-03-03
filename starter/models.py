from init import db

class Movie(db.Model):
     __tablename__ = 'Movie'

     id = db.Column(db.Integer, primary_key=True)
     title =  db.Column(db.String)
     release_date = db.Column(db.DateTime())

class Actors(db.Model):
    __tablename__ = 'Actors'

    name = db.Column(db.String)
    gender = db.Column(db.String(10))
    age = db.Column(db.Integer)