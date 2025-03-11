from app import db

class Area(db.Model):
    __tablename__ = "area"

    area_id = db.Column(db.Integer, primary_key=True)  # Primary Key
    area_name = db.Column(db.String(150), nullable=False)  # Area Name
    zone_id = db.Column(db.Integer, db.ForeignKey("zone.zone_id"), nullable=False)  # Foreign Key

    # Relationship to Zone model
    zone = db.relationship("Zone", back_populates="areas")  

    def __init__(self, area_name, zone_id):
        self.area_name = area_name
        self.zone_id = zone_id
