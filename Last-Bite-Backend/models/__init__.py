from app import db  # Import db from app.py

def init_db():
    """Initialize the database with the Flask app context."""
    db.create_all()
