from flask import Blueprint, jsonify, request
from services.user_subscription_service import *
from schemas.user_subscription_schema import UserSubscriptionSchema

subscription_bp = Blueprint("subscription_bp", __name__)

# Initialize Schema
subscription_schema = UserSubscriptionSchema()
subscriptions_schema = UserSubscriptionSchema(many=True)

# ✅ GET all subscriptions
@subscription_bp.route("/", methods=["GET"])
def get_subscriptions():
    subscriptions_list = get_all_subscriptions()
    return jsonify(subscriptions_schema.dump(subscriptions_list))

# ✅ GET a subscription by ID
@subscription_bp.route("/<int:subscription_id>", methods=["GET"])
def get_subscription(subscription_id):
    subscription = get_subscription_by_id(subscription_id)
    if subscription:
        return jsonify(subscription_schema.dump(subscription))
    return jsonify({"error": "Subscription not found"}), 404

# ✅ GET subscriptions by user
@subscription_bp.route("/user/<int:user_id>", methods=["GET"])
def get_user_subscriptions(user_id):
    subscriptions = get_subscriptions_by_user(user_id)
    return jsonify(subscriptions_schema.dump(subscriptions))

# ✅ CREATE a new subscription
@subscription_bp.route("/", methods=["POST"])
def add_subscription():
    data = request.get_json()

    # Validate input
    errors = subscription_schema.validate(data)
    if errors:
        return jsonify({"error": errors}), 400

    new_subscription = create_subscription(
        data["product_id"], data["user_id"], data["subscription_type"],
        data["start_date"], data["end_date"]
    )

    return jsonify(subscription_schema.dump(new_subscription)), 201

# ✅ UPDATE a subscription
@subscription_bp.route("/<int:subscription_id>", methods=["PUT"])
def modify_subscription(subscription_id):
    data = request.get_json()

    # Validate input
    errors = subscription_schema.validate(data)
    if errors:
        return jsonify({"error": errors}), 400

    updated_subscription = update_subscription(
        subscription_id, data["product_id"], data["user_id"], 
        data["subscription_type"], data["start_date"], data["end_date"]
    )

    if updated_subscription:
        return jsonify(subscription_schema.dump(updated_subscription))
    return jsonify({"error": "Subscription not found"}), 404

# ✅ DELETE a subscription
@subscription_bp.route("/<int:subscription_id>", methods=["DELETE"])
def remove_subscription(subscription_id):
    result = delete_subscription(subscription_id)
    if result:
        return jsonify(result)
    return jsonify({"error": "Subscription not found"}), 404
