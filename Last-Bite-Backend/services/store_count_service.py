from models.store_count import StoreCount
from app import db

def generate_store_count(store_id, user_id):

    new_store_count_entity = StoreCount(store_id=store_id, user_id=user_id)
    db.session.add(new_store_count_entity)
    db.session.commit()
    return new_store_count_entity

def get_store_counts():
    """Fetch all Store Count records from the database."""
    return StoreCount.query.all()

def get_store_count_by_store_and_user_id(store_id, user_id):
    """Fetch a Store Count entity by the IDs of the associated store and user."""
    return StoreCount.query.filter(StoreCount.store_id==store_id, StoreCount.user_id==user_id).first()

def update_store_count(store_count):
    """If Store Count entity that had already been added to the database is going to be generated, the count attribute value is increased."""
    store_count.count = StoreCount.count + 1
    db.session.commit()
    return store_count

def get_top_store_by_user_id(user_id):
    """Fetch the Store Count entites associated with a user."""
    return StoreCount.query.filter(StoreCount.user_id==user_id).order_by(StoreCount.count.desc()).first()

def get_least_visited_store_by_user_id(user_id):
    """Fetch the Store Count entities associated with a user."""
    return StoreCount.query.filter(StoreCount.user_id==user_id).order_by(StoreCount.count.asc()).first()
