from app import db
from enumerations.enums import Status
from datetime import datetime

class Order(db.Model):
    __tablename__ = "user_order"

    order_id = db.Column(db.Integer, primary_key=True)  # Unique order ID
    user_id = db.Column(db.Integer, db.ForeignKey("user.user_id"), nullable=False)  # Foreign key to User
    cart_id = db.Column(db.Integer, db.ForeignKey("cart.cart_id"), nullable=False)  # Foreign key to Cart
    creation_date = db.Column(db.Date, nullable=False, default=datetime.utcnow)  # Auto-generated date
    status = db.Column(db.Enum(Status, name="status_enum"), nullable=False)  # Order status enum
    billed_date = db.Column(db.Date, nullable=True)  # Date when the order was billed
    total_price = db.Column(db.Float, nullable=False)  # Total price of the order

    # Relationships
    user = db.relationship("User", back_populates="orders")
    cart = db.relationship("Cart", back_populates="order")

    def __init__(self, user_id, cart_id, status, total_price, billed_date=None):
        self.user_id = user_id
        self.cart_id = cart_id
        self.status = Status(status)  # Ensure valid enum value
        self.total_price = total_price
        self.billed_date = billed_date
