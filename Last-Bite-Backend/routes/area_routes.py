from flask import Blueprint, jsonify, request
from services.area_service import get_all_areas, get_area_by_id, create_area, update_area, delete_area
from schemas.area_schema import AreaSchema

area_bp = Blueprint("area_bp", __name__)

# Initialize schemas
area_schema = AreaSchema()
areas_schema = AreaSchema(many=True)

# GET all areas
@area_bp.route("/", methods=["GET"])
def get_areas():
    areas_list = get_all_areas()
    return jsonify(areas_schema.dump(areas_list))

# GET a single area by ID
@area_bp.route("/<int:area_id>", methods=["GET"])
def get_area(area_id):
    area = get_area_by_id(area_id)
    if area:
        return jsonify(area_schema.dump(area))
    return jsonify({"error": "Area not found"}), 404

# CREATE a new area (with schema validation)
@area_bp.route("/", methods=["POST"])
def add_area():
    data = request.get_json()

    # Validate input using schema
    errors = area_schema.validate(data)
    if errors:
        return jsonify(errors), 400

    new_area = create_area(data["area_name"], data["zone_id"])
    return jsonify(area_schema.dump(new_area)), 201

# UPDATE an area
@area_bp.route("/<int:area_id>", methods=["PUT"])
def modify_area(area_id):
    data = request.get_json()

    # Validate input using schema
    errors = area_schema.validate(data)
    if errors:
        return jsonify(errors), 400

    updated_area = update_area(area_id, data["area_name"], data["zone_id"])
    if updated_area:
        return jsonify(area_schema.dump(updated_area))
    return jsonify({"error": "Area not found"}), 404

# DELETE an area
@area_bp.route("/<int:area_id>", methods=["DELETE"])
def remove_area(area_id):
    result = delete_area(area_id)
    if result:
        return jsonify(result)
    return jsonify({"error": "Area not found"}), 404
