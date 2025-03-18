from app import db

class UserRating(db.Model):
    __tablename__ = "user_rating"

    rating_id = db.Column(db.Integer, primary_key=True)  # Unique rating ID
    product_id = db.Column(db.Integer, db.ForeignKey("product.product_id"), nullable=False)  # Foreign key to Product
    user_id = db.Column(db.Integer, db.ForeignKey("user.user_id"), nullable=False)  # Foreign key to User
    score = db.Column(db.Integer, nullable=False)  # Score given by the user

    # Relationships
    product = db.relationship("Product", back_populates="ratings")
    user = db.relationship("User", back_populates="ratings")

    def __init__(self, product_id, user_id, score):
        self.product_id = product_id
        self.user_id = user_id
        self.score = score
