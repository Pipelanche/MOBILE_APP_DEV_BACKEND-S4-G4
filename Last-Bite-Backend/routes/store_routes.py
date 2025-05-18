from flask import Blueprint, request, jsonify
from services.store_service import *
from schemas.store_schema import StoreSchema

store_bp = Blueprint("store_bp", __name__)

# Initialize Schema
store_schema = StoreSchema()
stores_schema = StoreSchema(many=True)

# ✅ GET all stores
@store_bp.route("/", methods=["GET"])
def get_stores():
    stores_list = get_all_stores()
    return jsonify(stores_schema.dump(stores_list))

# ✅ GET a store by ID
@store_bp.route("/<int:store_id>", methods=["GET"])
def get_store(store_id):
    store = get_store_by_id(store_id)
    if store:
        return jsonify(store_schema.dump(store))
    return jsonify({"error": "Store not found"}), 404

# ✅ CREATE a new store
@store_bp.route("/", methods=["POST"])
def add_store():
    data = request.get_json()

    # Validate input
    errors = store_schema.validate(data)
    if errors:
        return jsonify({"error": errors}), 400

    new_store = create_store(
        data["nit"], data["name"], data["address"],
        data["longitude"], data["latitude"], data["logo"]
    )

    if isinstance(new_store, dict):  # Handle error
        return jsonify(new_store), 409

    return jsonify(store_schema.dump(new_store)), 201

# ✅ UPDATE a store
@store_bp.route("/<int:store_id>", methods=["PUT"])
def modify_store(store_id):
    data = request.get_json()

    # Validate input
    errors = store_schema.validate(data)
    print(errors)
    if errors:
        return jsonify({"error": errors}), 400

    
    if data.get("logo") is None:
            updated_store = update_store(
        store_id, data["nit"], data["name"], data["address"],
        data["longitude"], data["latitude"], data["opens_at"], data["closes_at"]
    )
    else:
        updated_store = update_store(
        store_id, data["nit"], data["name"], data["address"],
        data["longitude"], data["latitude"], data["opens_at"], data["closes_at"], data["logo"]
    )

    print(updated_store.name)

    if isinstance(updated_store, dict):  # Handle error
        return jsonify(updated_store), 409

    if updated_store:
        return jsonify(store_schema.dump(updated_store))
    return jsonify({"error": "Store not found"}), 404

# ✅ DELETE a store
@store_bp.route("/<int:store_id>", methods=["DELETE"])
def remove_store(store_id):
    result = delete_store(store_id)
    if result:
        return jsonify(result)
    return jsonify({"error": "Store not found"}), 404

#Get nearby stores
@store_bp.route("/nearby", methods=["GET"])
def get_nearby():
    lat = request.args.get("lat", type=float)
    lon = request.args.get("lon", type=float)

    if lat is None or lon is None:
        return jsonify({"error": "Latitude and Longitude are required"}), 400

    stores = get_nearby_stores(lat, lon)
    print(stores)
    return jsonify(stores_schema.dump(stores))

@store_bp.route("/top", methods=["GET"])
def get_top_stores():
    top_stores = get_top_valuable_stores()
    return jsonify(stores_schema.dump(top_stores))
