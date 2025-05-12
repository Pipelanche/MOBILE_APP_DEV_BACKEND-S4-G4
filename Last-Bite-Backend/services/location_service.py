from models.location import Location
from app import db

def generate_location(latitude, longitude):

    new_location = Location(latitude=latitude, longitude=longitude)
    db.session.add(new_location)
    db.session.commit()
    return new_location

def get_locations_all():
    """Fetch all locations from the database."""
    return Location.query.all()

def get_location_by_coordinates(latitude,longitude):
    """Fetch a location by its coordinates."""
    return Location.query.filter(Location.latitude == latitude, Location.longitude == longitude).first()

def update_location_count(location):
    """If a location that had already been added to the database is going to be generated, its count attribute is increased."""
    # location.update({'count': Location.count + 1})
    location.count = Location.count + 1
    db.session.commit()
    return location
