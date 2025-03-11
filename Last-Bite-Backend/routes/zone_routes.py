from flask import Blueprint, jsonify, request
from services.zone_service import get_all_zones, get_zone_by_id, create_zone, update_zone, delete_zone
from schemas.zone_schema import ZoneSchema

zone_bp = Blueprint("zone_bp", __name__)

# Initialize schemas
zone_schema = ZoneSchema()
zones_schema = ZoneSchema(many=True)

# ✅ GET all zones (using schema serialization)
@zone_bp.route("/", methods=["GET"])
def get_zones():
    zones_list = get_all_zones()
    return jsonify(zones_schema.dump(zones_list))

# ✅ GET a single zone by ID
@zone_bp.route("/<int:zone_id>", methods=["GET"])
def get_zone(zone_id):
    zone = get_zone_by_id(zone_id)
    if zone:
        return jsonify(zone_schema.dump(zone))
    return jsonify({"error": "Zone not found"}), 404

# ✅ CREATE a new zone (with schema validation)
@zone_bp.route("/", methods=["POST"])
def add_zone():
    data = request.get_json()

    # Validate input using schema
    errors = zone_schema.validate(data)
    if errors:
        return jsonify(errors), 400

    new_zone = create_zone(data["zone_name"])
    return jsonify(zone_schema.dump(new_zone)), 201

# ✅ UPDATE a zone (with schema validation)
@zone_bp.route("/<int:zone_id>", methods=["PUT"])
def modify_zone(zone_id):
    data = request.get_json()

    # Validate input using schema
    errors = zone_schema.validate(data)
    if errors:
        return jsonify(errors), 400

    updated_zone = update_zone(zone_id, data["zone_name"])
    if updated_zone:
        return jsonify(zone_schema.dump(updated_zone))
    return jsonify({"error": "Zone not found"}), 404

# ✅ DELETE a zone
@zone_bp.route("/<int:zone_id>", methods=["DELETE"])
def remove_zone(zone_id):
    result = delete_zone(zone_id)
    if result:
        return jsonify(result)
    return jsonify({"error": "Zone not found"}), 404
