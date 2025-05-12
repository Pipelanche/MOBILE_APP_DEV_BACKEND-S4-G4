from flask import Blueprint, jsonify, request
from services.location_service import generate_location, get_locations_all, get_location_by_coordinates, update_location_count
from schemas.location_schema import LocationSchema

location_bp = Blueprint("location_bp", __name__)

# Initialize schemas
location_schema = LocationSchema()
locations_schema = LocationSchema(many=True)

# GENERATE a new location (with schema validation)
@location_bp.route("/", strict_slashes=False, methods=["POST"])
def add_location():
    
    data = request.get_json()

    # Validate input using schema
    errors = location_schema.validate(data)
    if errors:
        return jsonify(errors), 400
    
    repeated_location = get_location_by_coordinates(data["latitude"], data["longitude"])
    if repeated_location:
        updated_location = update_location_count(repeated_location)
        return jsonify(location_schema.dump(updated_location)), 202
    else:
        new_location = generate_location(data["latitude"], data["longitude"])
        return jsonify(location_schema.dump(new_location)), 201

# GET all locations
@location_bp.route("/", strict_slashes=False, methods=["GET"])
def get_locations():

    locations_list = get_locations_all()
    return jsonify(locations_schema.dump(locations_list)), 200

