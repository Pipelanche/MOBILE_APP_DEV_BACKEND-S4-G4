from models.cart import Cart
from app import db
from datetime import datetime
from enumerations.enums import Status

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
    existing_cart = Cart.query.filter(Cart.user_id == user_id, Cart.status.in_(["ACTIVE", "PAYMENT_PROGRESS", "PAYMENT_DECLINED"])).first()
    if existing_cart:
        # print("El cart ya existe.")
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

def get_active_cart(user_id):
    """Fetch the user's ACTIVE, PAYMENT_PROGRESS, or PAYMENT_DECLINED cart.
    If none exists, create a new ACTIVE cart.
    """
    existing_cart = Cart.query.filter(
        Cart.user_id == user_id,
        Cart.status.in_([
            Status.ACTIVE.value,
            Status.PAYMENT_PROGRESS.value,
            Status.PAYMENT_DECLINED.value
        ])
    ).first()

    if existing_cart:
        return existing_cart

    # 🆕 Create a new ACTIVE cart
    new_cart = Cart(
        user_id=user_id,
        status=Status.ACTIVE.value,
        status_date=datetime.today()
    )
    db.session.add(new_cart)
    db.session.commit()
    return new_cart
