from flask import Blueprint, jsonify
from services.zone_service import get_all_zones
zone_bp = Blueprint("zone_bp", __name__)

@zone_bp.route("/", methods=["GET"])
def get_zones():
    zones_list = get_all_zones()
    return jsonify(zones_list)
