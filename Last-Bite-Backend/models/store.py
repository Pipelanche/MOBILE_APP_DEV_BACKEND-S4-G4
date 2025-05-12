from app import db

class Store(db.Model):
    __tablename__ = "store"

    store_id = db.Column(db.Integer, primary_key=True)  # Unique store ID
    nit = db.Column(db.String(150), nullable=False, unique=True)  # Unique national identifier
    name = db.Column(db.String(150), nullable=False)  # Store name
    address = db.Column(db.String(240), nullable=False)  # Store address
    longitude = db.Column(db.Float, nullable=False)  # Longitude for Google Maps
    latitude = db.Column(db.Float, nullable=False)  # Latitude for Google Maps
    logo = db.Column(db.String(1000), nullable=False)  # Store logo URL

    #Relationship with users store that have all the users from the store
    users = db.relationship("UserStore", back_populates="store", cascade="all, delete-orphan")

    #Relationship with the store products
    products = db.relationship("Product", back_populates="store", cascade="all, delete-orphan")

    def __init__(self, nit, name, address, longitude, latitude, logo):
        self.nit = nit
        self.name = name
        self.address = address
        self.longitude = longitude
        self.latitude = latitude
        self.logo = logo