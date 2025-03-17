from app import db
from enumerations.enums import SubscriptionType  # Import Enum for subscription type

class UserSubscription(db.Model):
    __tablename__ = "user_subscription"

    subscription_id = db.Column(db.Integer, primary_key=True)  # Unique subscription ID
    product_id = db.Column(db.Integer, db.ForeignKey("product.product_id"), nullable=False)  # Foreign key to Product
    user_id = db.Column(db.Integer, db.ForeignKey("user.user_id"), nullable=False)  # Foreign key to User
    subscription_type = db.Column(db.Enum(SubscriptionType, name="subscription_type_enum"), nullable=False)  # Enum: WEEK, MONTH, YEAR
    start_date = db.Column(db.Date, nullable=False)  # Start date of the subscription
    end_date = db.Column(db.Date, nullable=False)  # End date of the subscription

    # Relationships
    product = db.relationship("Product", back_populates="subscriptions")
    user = db.relationship("User", back_populates="subscriptions")

    def __init__(self, product_id, user_id, subscription_type, start_date, end_date):
        self.product_id = product_id
        self.user_id = user_id
        self.subscription_type = SubscriptionType(subscription_type)  # Ensure valid Enum value
        self.start_date = start_date
        self.end_date = end_date
