from app import db
from models.cart import Cart
from models.product import Product
from enumerations.enums import Status

class CartProduct(db.Model):
    __tablename__ = "cart_product"

    cart_id = db.Column(db.Integer, db.ForeignKey("cart.cart_id"), primary_key=True, nullable=False)  # FK to Cart
    product_id = db.Column(db.Integer, db.ForeignKey("product.product_id"), primary_key=True, nullable=False)  # FK to Product

    # Relationships
    cart = db.relationship("Cart", back_populates="cart_products")
    product = db.relationship("Product", back_populates="cart_products")

    def __init__(self, cart_id, product_id):
        self.cart_id = cart_id
        self.product_id = product_id
