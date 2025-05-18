from flask import Blueprint, jsonify, request
from services.product_received_service import generate_product_received, get_received_products
from schemas.product_received_schema import ProductReceived

product_received_bp = Blueprint("product_received_bp", __name__)

# Initialize schemas
product_received_schema = ProductReceived()
products_received_schema = ProductReceived(many=True)

# GENERATE a new product received (with schema validation)
@product_received_bp.route("/", strict_slashes=False, methods=["POST"])
def add_product_schema():

    data = request.get_json()

    # Validate input using schema
    errors = product_received_schema.validate(data)
    if errors:
        return jsonify(errors), 400
    
    product_received = generate_product_received(data["image_string"])
    return jsonify(product_received_schema.dump(product_received)), 201

# GET all received products
@product_received_bp.route("/", strict_slashes=False, methods=["GET"])
def get_received_products():

    received_products_list = get_received_products()
    return jsonify(products_received_schema.dump(received_products_list)), 200
