from models.user_rating import UserRating
from app import db

def get_all_ratings():
    """Fetch all ratings from the database."""
    return UserRating.query.all()

def get_ratings_by_product(product_id):
    """Fetch all ratings for a specific product."""
    return UserRating.query.filter_by(product_id=product_id).all()

def get_ratings_by_user(user_id):
    """Fetch all ratings given by a specific user."""
    return UserRating.query.filter_by(user_id=user_id).all()

def get_rating_by_id(rating_id):
    """Fetch a single rating by ID."""
    return UserRating.query.get(rating_id)

def create_user_rating(product_id, user_id, score):
    """Create a new rating, ensuring a user can rate a product only once."""

    # Check if the user has already rated this product
    existing_rating = UserRating.query.filter_by(product_id=product_id, user_id=user_id).first()
    if existing_rating:
        return {"error": "User has already rated this product"}, 400  # HTTP 400 Bad Request

    new_rating = UserRating(product_id, user_id, score)
    db.session.add(new_rating)
    db.session.commit()
    return new_rating

def update_user_rating(rating_id, score):
    """Update an existing rating."""
    rating = UserRating.query.get(rating_id)
    if not rating:
        return None  # Rating not found

    rating.score = score
    db.session.commit()
    return rating

def delete_user_rating(rating_id):
    """Delete a rating from the database."""
    rating = UserRating.query.get(rating_id)
    if not rating:
        return None  # Rating not found

    db.session.delete(rating)
    db.session.commit()
    return {"message": f"Rating {rating_id} deleted successfully"}
