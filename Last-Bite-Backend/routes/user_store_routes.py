from flask import Blueprint, jsonify, request
from services.user_store_service import *
from schemas.user_store_schema import UserStoreSchema
from services.store_service import *
from schemas.store_schema import StoreSchema

user_store_bp = Blueprint("user_store_bp", __name__)

# Initialize Schema
user_store_schema = UserStoreSchema()
user_stores_schema = UserStoreSchema(many=True)

store_schema = StoreSchema()
stores_schema = StoreSchema(many=True)

# ✅ GET all user-store relationships
@user_store_bp.route("/", methods=["GET"])
def get_user_stores():
    user_stores = get_all_user_stores()
    return jsonify(user_stores_schema.dump(user_stores))

# ✅ GET stores for a specific user
@user_store_bp.route("/user/<int:user_id>", methods=["GET"])
def get_stores_by_user(user_id):
    stores = get_user_stores_by_user(user_id)
    return jsonify(user_stores_schema.dump(stores))

# ✅ GET stores for a specific user in store format
@user_store_bp.route("stores/user/<int:user_id>", methods=["GET"])
def get_all_stores_by_user(user_id):
    stores = get_all_user_stores_by_user(user_id)
    return jsonify(stores_schema.dump(stores))

# ✅ GET users for a specific store
@user_store_bp.route("/store/<int:store_id>", methods=["GET"])
def get_users_by_store(store_id):
    users = get_all_users_by_store(store_id)
    return jsonify(user_stores_schema.dump(users))

# ✅ ADD a user to a store
@user_store_bp.route("/", methods=["POST"])
def add_user_store():
    data = request.get_json()

    # Validate input
    errors = user_store_schema.validate(data)
    if errors:
        return jsonify({"error": errors}), 400

    new_relation = add_user_to_store(data["user_id"], data["store_id"])

    if isinstance(new_relation, dict):  # Handle error
        return jsonify(new_relation), 409

    return jsonify(user_store_schema.dump(new_relation)), 201

# ✅ REMOVE a user from a store
@user_store_bp.route("/user/<int:user_id>/store/<int:store_id>", methods=["DELETE"])
def delete_user_store(user_id, store_id):
    result = remove_user_from_store(user_id, store_id)
    if result:
        return jsonify(result)
    return jsonify({"error": "User-store relationship not found"}), 404
