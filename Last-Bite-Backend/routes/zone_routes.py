from flask import Blueprint, jsonify, request
from services.zone_service import *

zone_bp = Blueprint("zone_bp", __name__)

# ✅ GET all zones
@zone_bp.route("/", methods=["GET"])
def get_zones():
    zones_list = get_all_zones()
    return jsonify(zones_list)

# ✅ GET a single zone by ID
@zone_bp.route("/<int:zone_id>", methods=["GET"])
def get_zone(zone_id):
    zone = get_zone_by_id(zone_id)
    if zone:
        return jsonify(zone)
    return jsonify({"error": "Zone not found"}), 404

# ✅ CREATE a new zone
@zone_bp.route("/", methods=["POST"])
def add_zone():
    data = request.get_json()
    if "zone_name" not in data:
        return jsonify({"error": "zone_name is required"}), 400
    new_zone = create_zone(data["zone_name"])
    return jsonify(new_zone), 201

# ✅ UPDATE a zone
@zone_bp.route("/<int:zone_id>", methods=["PUT"])
def modify_zone(zone_id):
    data = request.get_json()
    if "zone_name" not in data:
        return jsonify({"error": "zone_name is required"}), 400
    updated_zone = update_zone(zone_id, data["zone_name"])
    if updated_zone:
        return jsonify(updated_zone)
    return jsonify({"error": "Zone not found"}), 404

# ✅ DELETE a zone
@zone_bp.route("/<int:zone_id>", methods=["DELETE"])
def remove_zone(zone_id):
    result = delete_zone(zone_id)
    if result:
        return jsonify(result)
    return jsonify({"error": "Zone not found"}), 404
