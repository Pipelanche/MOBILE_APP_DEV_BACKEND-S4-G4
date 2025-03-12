from app import db
from enumerations.enums import ProductType  # Import Enum for product type

class Product(db.Model):
    __tablename__ = "product"

    product_id = db.Column(db.Integer, primary_key=True)  # Unique product ID
    store_id = db.Column(db.Integer, db.ForeignKey("store.store_id"), nullable=False)  # Foreign key to Store
    name = db.Column(db.String(150), nullable=False)  # Product name
    product_type = db.Column(db.Enum(ProductType, name="product_type_enum"), nullable=False)  # Enum: PRODUCT, SUBSCRIPTION
    unit_price = db.Column(db.Float, nullable=False)  # Price of one unit
    detail = db.Column(db.String(240), nullable=True)  # Optional description
    score = db.Column(db.Float, nullable=True)  # Average rating
    image = db.Column(db.String(1000), nullable=False)  # Image URL

    # Relationship to Store model
    store = db.relationship("Store", back_populates="products")

    def __init__(self, store_id, name, product_type, unit_price, detail, score, image):
        self.store_id = store_id
        self.name = name
        self.product_type = ProductType(product_type)  # Ensure valid Enum value
        self.unit_price = unit_price
        self.detail = detail
        self.score = score
        self.image = image
