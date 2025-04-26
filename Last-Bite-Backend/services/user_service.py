from models.user import User
from app import db
from models.signup_events import SignupEvent
from datetime import datetime, timezone

def get_all_users():
    """Fetch all users from the database."""
    return User.query.all()

def get_user_by_id(user_id):
    """Fetch a single user by ID."""
    return User.query.get(user_id)

def create_user(name, user_email, mobile_number, area_id, verification_code, user_type, description=None):
    """Create a new user."""
    new_user = User(name=name, user_email=user_email, mobile_number=mobile_number, verification_code = verification_code, area_id=area_id, user_type=user_type, description=description)
    db.session.add(new_user)
    db.session.commit()
    return new_user

def update_user(user_id, name, user_email, mobile_number, area_id, verification_code, user_type, description=None):
    """Update an existing user."""
    user = User.query.get(user_id)
    if user:
        user.name = name
        user.user_email = user_email
        user.mobile_number = mobile_number
        user.area_id = area_id
        user.verification_code = verification_code
        user.user_type = user_type
        user.description = description
        db.session.commit()
        return user
    return None

def delete_user(user_id):
    """Delete a user."""
    user = User.query.get(user_id)
    if user:
        db.session.delete(user)
        db.session.commit()
        return {"message": f"User {user_id} deleted successfully"}
    return None

def get_user_by_email(email):
    """Fetch a user by their email."""
    return User.query.filter_by(user_email=email).first()

def update_signup_event(user_id, attempt_id):
    event = SignupEvent.query.filter_by(attempt_id=attempt_id).first()
    print(event)
    if event:
        event.user_id = user_id
        event.completed_at = datetime.utcnow()
        event.status = 'completed'

    db.session.commit()
    return event

def get_conversion_rate():
    completed = SignupEvent.query.filter_by(status='completed').all()
    attempts = SignupEvent.query.filter_by(status='started').all()
    total = len(completed) + len(attempts)
    conversion_rate = len(completed) / total
    return {
        "completed": len(completed),
        "attempts": len(attempts),
        "total": total,
        "conversion_rate": conversion_rate
    }




    