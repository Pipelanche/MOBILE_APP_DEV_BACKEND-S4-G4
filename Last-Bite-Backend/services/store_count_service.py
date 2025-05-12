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