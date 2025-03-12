from models.store import Store
from app import db

def get_all_stores():
    """Fetch all stores from the database."""
    return Store.query.all()

def get_store_by_id(store_id):
    """Fetch a single store by ID."""
    return Store.query.get(store_id)

def create_store(nit, name, address, longitude, latitude, logo):
    """Create a new store in the database."""
    existing_store = Store.query.filter_by(nit=nit).first()
    if existing_store:
        return {"error": "Store with this NIT already exists"}, 409  # Conflict error

    new_store = Store(nit, name, address, longitude, latitude, logo)
    db.session.add(new_store)
    db.session.commit()
    return new_store

def update_store(store_id, nit, name, address, longitude, latitude, logo):
    """Update an existing store."""
    store = Store.query.get(store_id)
    if not store:
        return None  # Store not found

    # Ensure NIT is unique
    existing_store = Store.query.filter(Store.nit == nit, Store.store_id != store_id).first()
    if existing_store:
        return {"error": "Store with this NIT already exists"}, 409  # Conflict error

    store.nit = nit
    store.name = name
    store.address = address
    store.longitude = longitude
    store.latitude = latitude
    store.logo = logo

    db.session.commit()
    return store

def delete_store(store_id):
    """Delete a store from the database."""
    store = Store.query.get(store_id)
    if not store:
        return None  # Store not found

    db.session.delete(store)
    db.session.commit()
    return {"message": f"Store {store_id} deleted successfully"}
