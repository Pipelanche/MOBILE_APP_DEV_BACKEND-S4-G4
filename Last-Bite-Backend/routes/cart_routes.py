from flask import Blueprint, jsonify, request
from services.cart_service import *
from schemas.cart_schema import CartSchema

cart_bp = Blueprint("cart_bp", __name__)

# Initialize Schema
cart_schema = CartSchema()
carts_schema = CartSchema(many=True)

# ✅ GET all carts
@cart_bp.route("/", methods=["GET"])
def get_carts():
    carts_list = get_all_carts()
    return jsonify(carts_schema.dump(carts_list))

# ✅ GET carts by user
@cart_bp.route("/user/<int:user_id>", methods=["GET"])
def get_carts_by_user_route(user_id):
    carts = get_carts_by_user(user_id)
    return jsonify(carts_schema.dump(carts))

# ✅ GET a cart by ID
@cart_bp.route("/<int:cart_id>", methods=["GET"])
def get_cart(cart_id):
    cart = get_cart_by_id(cart_id)
    if cart:
        return jsonify(cart_schema.dump(cart))
    return jsonify({"error": "Cart not found"}), 404

# ✅ CREATE a new cart
@cart_bp.route("/", methods=["POST"])
def add_cart():
    data = request.get_json()

    # Validate input
    errors = cart_schema.validate(data)
    if errors:
        return jsonify({"error": errors}), 400

    new_cart = create_cart(data["user_id"], data["status"])
    
    if isinstance(new_cart, dict):  # Check if it returned an error
        return jsonify(new_cart), 400

    return jsonify(cart_schema.dump(new_cart)), 201

# ✅ UPDATE a cart status
@cart_bp.route("/<int:cart_id>/status", methods=["PUT"])
def modify_cart_status(cart_id):
    data = request.get_json()

    # Validate input
    errors = cart_schema.validate(data)
    if errors:
        return jsonify({"error": errors}), 400

    updated_cart = update_cart_status(cart_id, data["status"])
    if updated_cart:
        return jsonify(cart_schema.dump(updated_cart))
    return jsonify({"error": "Cart not found"}), 404

# ✅ DELETE a cart (Soft delete)
@cart_bp.route("/<int:cart_id>", methods=["DELETE"])
def remove_cart(cart_id):
    result = delete_cart(cart_id)
    if result:
        return jsonify(result)
    return jsonify({"error": "Cart not found"}), 404
