from init import db

class Movie(db.Model):
     __tablename__ = 'Movie'

     id = db.Column(db.Integer, primary_key=True)
     title =  db.Column(db.String)
     release_date = db.Column(db.DateTime())
     
     def __init__(self, title, release_date):
        self.title = title
        self.release_date = release_date
    
     def format(self):
        return {
            'id': self.id,
            'title': self.title,
            'release_date': self.release_date
        }


class Actors(db.Model):
    __tablename__ = 'Actors'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    gender = db.Column(db.String(10))
    age = db.Column(db.Integer)