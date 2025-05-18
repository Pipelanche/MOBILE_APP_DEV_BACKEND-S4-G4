from app import db

class Location(db.Model):
    __tablename__ = "location"

    location_id = db.Column(db.Integer, primary_key=True)
    latitude = db.Column(db.Float, nullable=False)
    longitude = db.Column(db.Float, nullable=False)
    count = db.Column(db.Integer, nullable=False)

    def __init__(self, latitude, longitude):
        
        self.latitude = latitude
        self.longitude = longitude
        self.count = 1

from app import db

class Location(db.Model):
    __tablename__ = "location"

    location_id = db.Column(db.Integer, primary_key=True)
    latitude = db.Column(db.Float, nullable=False)
    longitude = db.Column(db.Float, nullable=False)
    count = db.Column(db.Integer, nullable=False)

    def __init__(self, latitude, longitude):
        
        self.latitude = latitude
        self.longitude = longitude
        self.count = 1

