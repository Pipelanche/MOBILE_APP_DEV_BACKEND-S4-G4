from flask import Blueprint, jsonify, request
from services.cart_product_service import *
from schemas.cart_product_schema import CartProductSchema

cart_product_bp = Blueprint("cart_product_bp", __name__)

# Initialize Schema
cart_product_schema = CartProductSchema()
cart_products_schema = CartProductSchema(many=True)

# ✅ GET all products in a cart
@cart_product_bp.route("/cart/<int:cart_id>", methods=["GET"])
def get_products_in_cart_route(cart_id):
    products = get_products_in_cart(cart_id)
    return jsonify(cart_products_schema.dump(products))

# ✅ ADD or UPDATE a product in a cart
@cart_product_bp.route("/", methods=["POST"])
def add_or_update_product_in_cart_route():
    data = request.get_json()

    # Validate input
    errors = cart_product_schema.validate(data)
    if errors:
        return jsonify({"error": errors}), 400

    cart_id = data["cart_id"]
    product_id = data["product_id"]
    quantity = data.get("quantity", 1)  # Default to 1 if not provided

    new_cart_product = add_product_to_cart(cart_id, product_id, quantity)

    if isinstance(new_cart_product, dict):  # Check for error responses
        return jsonify(new_cart_product), new_cart_product[1]  # Return error code

    return jsonify(cart_product_schema.dump(new_cart_product)), 201

# ✅ UPDATE product quantity in a cart
@cart_product_bp.route("/cart/<int:cart_id>/product/<int:product_id>", methods=["PUT"])
def update_product_quantity_route(cart_id, product_id):
    data = request.get_json()

    if "quantity" not in data:
        return jsonify({"error": "Quantity is required"}), 400

    result = update_product_quantity(cart_id, product_id, data["quantity"])
    return jsonify(result)

# ✅ REMOVE a product from a cart
@cart_product_bp.route("/cart/<int:cart_id>/product/<int:product_id>", methods=["DELETE"])
def remove_product_from_cart_route(cart_id, product_id):
    result = remove_product_from_cart(cart_id, product_id)
    return jsonify(result)
