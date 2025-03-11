from app import db

class Zone(db.Model):
    __tablename__ = "zone"
    zone_id = db.Column(db.Integer, primary_key=True)
    zone_name = db.Column(db.String(150), nullable=False)
