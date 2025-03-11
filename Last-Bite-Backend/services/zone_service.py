from models.zone import Zone
from app import db

def get_all_zones():
    zones = Zone.query.all()
    return [{"zone_id": z.zone_id, "zone_name": z.zone_name} for z in zones]

def get_zone_by_id(zone_id):
    zone = Zone.query.get(zone_id)
    if zone:
        return {"zone_id": zone.zone_id, "zone_name": zone.zone_name}
    return None

def create_zone(zone_name):
    new_zone = Zone(zone_name=zone_name)
    db.session.add(new_zone)
    db.session.commit()
    return {"zone_id": new_zone.zone_id, "zone_name": new_zone.zone_name}

def update_zone(zone_id, new_name):
    zone = Zone.query.get(zone_id)
    if zone:
        zone.zone_name = new_name
        db.session.commit()
        return {"zone_id": zone.zone_id, "zone_name": zone.zone_name}
    return None

def delete_zone(zone_id):
    zone = Zone.query.get(zone_id)
    if zone:
        db.session.delete(zone)
        db.session.commit()
        return {"message": f"Zone {zone_id} deleted successfully"}
    return None