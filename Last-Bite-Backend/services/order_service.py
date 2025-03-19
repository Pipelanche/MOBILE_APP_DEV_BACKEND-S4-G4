from models.order import Order
from models.cart import Cart
from models.user import User
from app import db
from datetime import datetime

def get_all_orders():
    """Fetch all orders from the database."""
    return Order.query.all()

def get_order_by_id(order_id):
    """Fetch a single order by ID."""
    return Order.query.get(order_id)

def get_orders_by_user(user_id):
    """Fetch all orders for a specific user."""
    return Order.query.filter_by(user_id=user_id).all()

def create_order(user_id, cart_id, status, total_price):
    """Create a new order."""
    
    # Check if user exists
    user = User.query.get(user_id)
    if not user:
        return {"error": "User not found"}, 404

    # Check if cart exists
    cart = Cart.query.get(cart_id)
    if not cart:
        return {"error": "Cart not found"}, 404

    # Ensure the cart is not already billed
    if cart.status == "BILLED":
        return {"error": "Cart has already been billed"}, 400

    new_order = Order(user_id, cart_id, status, total_price)
    db.session.add(new_order)
    db.session.commit()
    return new_order

def update_order(order_id, status, total_price):
    """Update an existing order."""
    order = Order.query.get(order_id)
    if not order:
        return None  # Order not found

    order.status = status
    order.total_price = total_price

    # If status is changed to BILLED, set billed_date
    if status == "BILLED" and order.billed_date is None:
        order.billed_date = datetime.utcnow()

    db.session.commit()
    return order

def delete_order(order_id):
    """Delete an order from the database."""
    order = Order.query.get(order_id)
    if not order:
        return None  # Order not found

    db.session.delete(order)
    db.session.commit()
    return {"message": f"Order {order_id} deleted successfully"}
