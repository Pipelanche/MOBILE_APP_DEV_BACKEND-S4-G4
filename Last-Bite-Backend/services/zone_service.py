from models.zone import Zone
from app import db  # Import the database instance

def get_all_zones():
    zones = Zone.query.all()
    return [{"zone_id": z.zone_id, "zone_name": z.zone_name} for z in zones]
