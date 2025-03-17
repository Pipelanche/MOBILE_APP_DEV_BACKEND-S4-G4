from models.user_subscription import UserSubscription
from app import db
from datetime import datetime

def get_all_subscriptions():
    """Fetch all user subscriptions from the database."""
    return UserSubscription.query.all()

def get_subscription_by_id(subscription_id):
    """Fetch a single subscription by ID."""
    return UserSubscription.query.get(subscription_id)

def get_subscriptions_by_user(user_id):
    """Fetch all subscriptions for a specific user."""
    return UserSubscription.query.filter_by(user_id=user_id).all()

def create_subscription(product_id, user_id, subscription_type, start_date, end_date):
    """Create a new user subscription."""
    # Convert date strings to date objects
    start_date = datetime.strptime(start_date, "%Y-%m-%d").date()
    end_date = datetime.strptime(end_date, "%Y-%m-%d").date()
    new_subscription = UserSubscription(product_id, user_id, subscription_type, start_date, end_date)
    db.session.add(new_subscription)
    db.session.commit()
    return new_subscription

def update_subscription(subscription_id, product_id, user_id, subscription_type, start_date, end_date):
    """Update an existing subscription."""
    start_date = datetime.strptime(start_date, "%Y-%m-%d").date()
    end_date = datetime.strptime(end_date, "%Y-%m-%d").date()
    subscription = UserSubscription.query.get(subscription_id)
    if not subscription:
        return None  # Subscription not found

    subscription.product_id = product_id
    subscription.user_id = user_id
    subscription.subscription_type = subscription_type
    subscription.start_date = start_date
    subscription.end_date = end_date

    db.session.commit()
    return subscription

def delete_subscription(subscription_id):
    """Delete a subscription from the database."""
    subscription = UserSubscription.query.get(subscription_id)
    if not subscription:
        return None  # Subscription not found

    db.session.delete(subscription)
    db.session.commit()
    return {"message": f"Subscription {subscription_id} deleted successfully"}
