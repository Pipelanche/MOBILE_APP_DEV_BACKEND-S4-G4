from app import db

class ProductTag(db.Model):
    __tablename__ = "product_tag"

    product_tag_id = db.Column(db.Integer, primary_key=True)  # Unique product tag ID
    product_id = db.Column(db.Integer, db.ForeignKey("product.product_id"), nullable=False)  # Foreign key to Product
    value = db.Column(db.String(30), nullable=False)  # The tag value (e.g., "150g", "4pcs")

    # Relationship with Product
    product = db.relationship("Product", back_populates="tags")

    def __init__(self, product_id, value):
        self.product_id = product_id
        self.value = value
