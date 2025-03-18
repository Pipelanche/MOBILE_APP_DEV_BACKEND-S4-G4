from app import db
from enumerations.enums import Status  # Import Enum for cart status
from datetime import datetime

class Cart(db.Model):
    __tablename__ = "cart"

    cart_id = db.Column(db.Integer, primary_key=True)  # Unique cart ID
    user_id = db.Column(db.Integer, db.ForeignKey("user.user_id"), nullable=False)  # Foreign key to User
    creation_date = db.Column(db.Date, nullable=False, default=datetime.utcnow)  # Creation date
    status = db.Column(db.Enum(Status, name="cart_status_enum"), nullable=False)  # Enum: ACTIVE, PAYMENT_PROGRESS, BILLED, DISABLED
    status_date = db.Column(db.Date, nullable=True)  # Date when status was last updated

    # Relationship with User
    user = db.relationship("User", back_populates="carts")

    #Relationship with cart products
    cart_products = db.relationship("CartProduct", back_populates="cart", cascade="all, delete-orphan")

    def __init__(self, user_id, status, status_date=None):
        self.user_id = user_id
        self.status = Status(status)  # Ensure it's a valid enum
        self.status_date = status_date if status_date else datetime.utcnow()
