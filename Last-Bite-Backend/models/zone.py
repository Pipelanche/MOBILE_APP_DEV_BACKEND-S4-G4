from app import db

class Zone(db.Model):
    __tablename__ = "zone"
    zone_id = db.Column(db.Integer, primary_key=True)
    zone_name = db.Column(db.String(150), nullable=False)

    # Relationship to Area model
    areas = db.relationship("Area", back_populates="zone", cascade="all, delete-orphan")

    def __init__(self, zone_name):
        self.zone_name = zone_name