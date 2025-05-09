from flask import Blueprint, jsonify, request
from services.user_service import *
from schemas.user_schema import UserSchema
from schemas.signup_event_schema import SignupEventSchema
from models.signup_events import SignupEvent

user_bp = Blueprint("user_bp", __name__)

# Initialize schemas
user_schema = UserSchema()
users_schema = UserSchema(many=True)
signups_schema = SignupEventSchema(many=True)

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
    print("Adding new user...")
    data = request.get_json()
    print(data["attempt_id"])
    # Validate input using schema
    errors = user_schema.validate(data)
    if errors:
        return jsonify(errors), 400
    new_user = create_user(data["name"], data["user_email"], data["mobile_number"], data["area_id"],  data.get("verification_code"), data["user_type"], data.get("description"))
    update_signup_event(new_user.user_id, data["attempt_id"])
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

# ✅ CREATE a signup event
@user_bp.route('/signup_events', methods=['POST'])
def create_signup_event():
    print("Creating signup event...")
    # Inserta intento
    event = SignupEvent()
    db.session.add(event)
    db.session.commit()
    
    return jsonify({'attempt_id': event.attempt_id}), 201

# ✅ GET signup attempts vs completed
@user_bp.route('/conversion_rate', methods=['GET'])
def get_signup_attempts_vs_completed():
    result = get_conversion_rate()
    return result

# ✅ Get all signup events
@user_bp.route('/signup_events', methods=['GET'])
def get_signup_events():
    print('llegue')
    signup_list = get_all_signup_events()
    return jsonify(signups_schema.dump(signup_list)), 201