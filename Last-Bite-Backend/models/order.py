from app import db
from enumerations.enums import Status
from datetime import datetime

class Order(db.Model):
    __tablename__ = "user_order"

    order_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.user_id"), nullable=False)
    cart_id = db.Column(db.Integer, db.ForeignKey("cart.cart_id"), nullable=False)
    creation_date = db.Column(db.Date, nullable=False, default=datetime.utcnow)
    status = db.Column(db.Enum(Status, name="status_enum"), nullable=False)
    billed_date = db.Column(db.Date, nullable=True)
    total_price = db.Column(db.Float, nullable=False)

    enabled = db.Column(db.Boolean, nullable=False, default=True) 

    # Relationships
    user = db.relationship("User", back_populates="orders")
    cart = db.relationship("Cart", back_populates="order")

    def __init__(self, user_id, cart_id, status, total_price, billed_date=None, enabled=True):
        self.user_id = user_id
        self.cart_id = cart_id
        self.status = Status(status)
        self.total_price = total_price
        self.billed_date = billed_date
        self.enabled = enabled 
