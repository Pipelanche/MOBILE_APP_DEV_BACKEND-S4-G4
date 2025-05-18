from app import db
from datetime import datetime
from sqlalchemy.sql import func as sqlalchemy_func

class Store(db.Model):
    __tablename__ = "store"

    store_id = db.Column(db.Integer, primary_key=True)  # Unique store ID
    nit = db.Column(db.String(150), nullable=False, unique=True)  # Unique national identifier
    name = db.Column(db.String(150), nullable=False)  # Store name
    address = db.Column(db.String(240), nullable=False)  # Store address
    longitude = db.Column(db.Float, nullable=False)  # Longitude for Google Maps
    latitude = db.Column(db.Float, nullable=False)  # Latitude for Google Maps
    logo = db.Column(db.String(1000), nullable=False)  # Store logo URL
    opens_at = db.Column(db.Time, nullable=False, server_default='00:00:00')
    closes_at = db.Column(db.Time, nullable=False, server_default='00:00:00')
    created_at = db.Column(db.DateTime, nullable=False, server_default=sqlalchemy_func.now()) # Usar server_default
    updated_at = db.Column(db.DateTime, nullable=False, server_default=sqlalchemy_func.now(), onupdate=sqlalchemy_func.now())

    #Relationship with users store that have all the users from the store
    users = db.relationship("UserStore", back_populates="store", cascade="all, delete-orphan")

    #Relationship with the store products
    products = db.relationship("Product", back_populates="store", cascade="all, delete-orphan")

    def __init__(self, nit, name, address, longitude, latitude, logo, opens_at, closes_at):
        self.nit = nit
        self.name = name
        self.address = address
        self.longitude = longitude
        self.latitude = latitude
        self.logo = logo
        self.opens_at = opens_at
        self.closes_at = closes_at
        self.created_at = datetime.now()
        self.updated_at = datetime.now()