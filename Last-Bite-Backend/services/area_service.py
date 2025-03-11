from models.area import Area
from app import db

def get_all_areas():
    """Fetch all areas from the database."""
    return Area.query.all()

def get_area_by_id(area_id):
    """Fetch a single area by its ID."""
    return Area.query.get(area_id)

def create_area(area_name, zone_id):
    """Create a new area linked to a zone."""
    new_area = Area(area_name=area_name, zone_id=zone_id)
    db.session.add(new_area)
    db.session.commit()
    return new_area

def update_area(area_id, new_name, zone_id):
    """Update an existing area's name and zone."""
    area = Area.query.get(area_id)
    if area:
        area.area_name = new_name
        area.zone_id = zone_id  # Allow moving areas to different zones
        db.session.commit()
        return area
    return None

def delete_area(area_id):
    """Delete an area."""
    area = Area.query.get(area_id)
    if area:
        db.session.delete(area)
        db.session.commit()
        return {"message": f"Area {area_id} deleted successfully"}
    return None
