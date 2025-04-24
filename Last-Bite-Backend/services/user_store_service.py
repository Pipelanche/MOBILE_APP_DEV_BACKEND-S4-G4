from models.user_store import UserStore
from models.user import User
from app import db

def get_all_user_stores():
    """Fetch all user-store relationships."""
    return UserStore.query.all()

def get_user_stores_by_user(user_id):
    """Fetch all stores linked to a specific user."""
    return UserStore.query.filter_by(user_id=user_id).all()

def get_all_user_stores_by_user(user_id):
    user_stores = UserStore.query.filter_by(user_id=user_id).all()
    return [user_store.store for user_store in user_stores] 

def get_all_users_by_store(store_id):
    """Fetch all users linked to a specific store."""
    return UserStore.query.filter_by(store_id=store_id).all()

def add_user_to_store(user_id, store_id):
    """Add a user to a store if they are of type 'STORE'."""
    
    # ✅ Check if the user exists
    user = User.query.get(user_id)
    if not user:
        return {"error": "User not found"}, 404  # Not Found error

    # ✅ Ensure the user is of type "STORE"
    if "STORE" not in user.user_type.value:  # Assuming user_type is an Enum
        return {"error": "User must have 'STORE' as user_type"}, 403  # Forbidden error

    # ✅ Check if the relationship already exists
    existing_relation = UserStore.query.filter_by(user_id=user_id, store_id=store_id).first()
    if existing_relation:
        return {"error": "User is already linked to this store"}, 409  # Conflict error

    # ✅ Add the user to the store
    new_relation = UserStore(user_id=user_id, store_id=store_id)
    db.session.add(new_relation)
    db.session.commit()
    return new_relation


def remove_user_from_store(user_id, store_id):
    """Remove a user from a store."""
    relation = UserStore.query.filter_by(user_id=user_id, store_id=store_id).first()
    if not relation:
        return None  # Relationship not found

    db.session.delete(relation)
    db.session.commit()
    return {"message": f"User {user_id} removed from store {store_id}"}
