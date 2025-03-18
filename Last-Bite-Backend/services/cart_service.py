from models.cart import Cart
from app import db
from datetime import datetime

def get_all_carts():
    """Fetch all carts from the database."""
    return Cart.query.all()

def get_carts_by_user(user_id):
    """Fetch all carts for a specific user."""
    return Cart.query.filter_by(user_id=user_id).all()

def get_cart_by_id(cart_id):
    """Fetch a single cart by ID."""
    return Cart.query.get(cart_id)

def create_cart(user_id, status):
    """Create a new cart, ensuring only one ACTIVE or PAYMENT_PROGRESS cart per user."""
    
    # Check if user already has an ACTIVE or PAYMENT_PROGRESS cart
    existing_cart = Cart.query.filter(Cart.user_id == user_id, Cart.status.in_(["ACTIVE", "PAYMENT_PROGRESS"])).first()
    if existing_cart:
        return {"error": "User already has an active or payment in-progress cart"}, 400

    new_cart = Cart(user_id, status)
    db.session.add(new_cart)
    db.session.commit()
    return new_cart

def update_cart_status(cart_id, status):
    """Update the status of a cart."""
    cart = Cart.query.get(cart_id)
    if not cart:
        return None  # Cart not found

    cart.status = status
    cart.status_date = datetime.utcnow()  # Update status date
    db.session.commit()
    return cart

def delete_cart(cart_id):
    """Delete a cart from the database (soft delete by setting status to DISABLED)."""
    cart = Cart.query.get(cart_id)
    if not cart:
        return None  # Cart not found

    cart.status = "DISABLED"
    cart.status_date = datetime.utcnow()
    db.session.commit()
    return {"message": f"Cart {cart_id} disabled successfully"}
