from flask import Blueprint, jsonify, request
from services.user_service import *
from schemas.user_schema import UserSchema

user_bp = Blueprint("user_bp", __name__)

# Initialize schemas
user_schema = UserSchema()
users_schema = UserSchema(many=True)

# ✅ GET all users
@user_bp.route("/", methods=["GET"])
def get_users():
    users_list = get_all_users()
    return jsonify(users_schema.dump(users_list))

# ✅ GET a single user by ID
@user_bp.route("/<int:user_id>", methods=["GET"])
def get_user(user_id):
    user = get_user_by_id(user_id)
    if user:
        return jsonify(user_schema.dump(user))
    return jsonify({"error": "User not found"}), 404

# ✅ CREATE a new user
@user_bp.route("/", methods=["POST"])
def add_user():
    data = request.get_json()

    # Validate input using schema
    errors = user_schema.validate(data)
    if errors:
        return jsonify(errors), 400

    new_user = create_user(data["name"], data["user_email"], data["mobile_number"], data["area_id"],  data.get("verification_code"), data["user_type"], data.get("description"))
    return jsonify(user_schema.dump(new_user)), 201

# ✅ UPDATE a user
@user_bp.route("/<int:user_id>", methods=["PUT"])
def modify_user(user_id):
    data = request.get_json()

    # Validate input using schema
    errors = user_schema.validate(data)
    if errors:
        return jsonify(errors), 400

    updated_user = update_user(user_id, data["name"], data["user_email"], data["mobile_number"], data["area_id"], data["verification_code"], data["user_type"], data.get("description"))
    if updated_user:
        return jsonify(user_schema.dump(updated_user))
    return jsonify({"error": "User not found"}), 404

# ✅ DELETE a user
@user_bp.route("/<int:user_id>", methods=["DELETE"])
def remove_user(user_id):
    result = delete_user(user_id)
    if result:
        return jsonify(result)
    return jsonify({"error": "User not found"}), 404

# ✅ GET a user by email
@user_bp.route("/email", methods=["GET"])
def get_user_by_email_route():
    email = request.args.get("email")

    if not email:
        return jsonify({"error": "Email query parameter is required"}), 400

    user = get_user_by_email(email)
    if user:
        return jsonify(user_schema.dump(user))
    return jsonify({"error": "User not found"}), 404
