from flask import Blueprint, jsonify

zone_bp = Blueprint("zone_bp", __name__)

@zone_bp.route("/", methods=["GET"])
def get_zones():
    return jsonify({"message": "Zone endpoint is working!"})
