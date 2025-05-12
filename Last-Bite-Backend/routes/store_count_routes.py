from flask import Blueprint, jsonify, request
from services.store_count_service import generate_store_count, get_store_count_by_store_and_user_id, update_store_count
from schemas.store_count_schema import StoreCountSchema


store_count_bp = Blueprint("store_count_bp", __name__)

# Initialize schemas
store_count_schema = StoreCountSchema()
store_counts_schema = StoreCountSchema(many=True)

# GENERATE a new store count (with schema validation)
@store_count_bp.route("/", strict_slashes=False, methods=["POST"])
def add_store_count():

    data = request.get_json()

    # Validate input using schema
    errors = store_count_schema.validate(data)
    if errors:
        return jsonify(errors), 400
    
    repeated_store_count = get_store_count_by_store_and_user_id(data["store_id"], data["user_id"])
    if repeated_store_count:
        updated_store_count = update_store_count(repeated_store_count)
        return jsonify(store_count_schema.dump(updated_store_count)), 202
    else:
        new_store_count = generate_store_count(data["store_id"], data["user_id"])
        return jsonify(store_count_schema.dump(new_store_count)), 201
    
# GET all Store Count rows
@store_count_bp.route("/", strict_slashes=False, methods=["GET"])
def get_store_counts_all():

    store_counts_list = get_store_counts_all()
    return jsonify(store_counts_schema.dump(store_counts_list)), 200