from flask import Blueprint, jsonify, request
from services.order_service import *
from schemas.order_schema import OrderSchema, OrderUpdateSchema

order_bp = Blueprint("order_bp", __name__)

# Initialize Schema
order_schema = OrderSchema()
orders_schema = OrderSchema(many=True)
order_update_schema = OrderUpdateSchema() 

# ✅ GET all orders
@order_bp.route("/", methods=["GET"])
def get_orders():
    orders_list = get_all_orders()
    return jsonify(orders_schema.dump(orders_list))

# ✅ GET order by ID
@order_bp.route("/<int:order_id>", methods=["GET"])
def get_order(order_id):
    order = get_order_by_id(order_id)
    if order:
        return jsonify(order_schema.dump(order))
    return jsonify({"error": "Order not found"}), 404

# ✅ GET orders by user
@order_bp.route("/user/<int:user_id>", methods=["GET"])
def get_user_orders(user_id):
    orders = get_orders_by_user(user_id)
    return jsonify(orders_schema.dump(orders))

# ✅ CREATE an order
@order_bp.route("/", methods=["POST"])
def add_order():
    data = request.get_json()

    # Validate input
    errors = order_schema.validate(data)
    if errors:
        return jsonify({"error": errors}), 400

    new_order = create_order(data["user_id"], data["cart_id"], data["status"], data["total_price"])

    if isinstance(new_order, dict):  # Check if it returned an error
        return jsonify(new_order), 400

    return jsonify(order_schema.dump(new_order)), 201

# ✅ UPDATE an order
@order_bp.route("/<int:order_id>", methods=["PUT"])
def modify_order(order_id):
    data = request.get_json()
    
    # Validate input
    errors = order_update_schema.validate(data)
    if errors:
        return jsonify({"error": errors}), 400

    updated_order = update_order(order_id, data["status"], data["total_price"])
    if updated_order:
        return jsonify(order_update_schema.dump(updated_order))
    return jsonify({"error": "Order not found"}), 404

# ✅ DELETE an order
@order_bp.route("/<int:order_id>", methods=["DELETE"])
def remove_order(order_id):
    result = delete_order(order_id)
    if result:
        return jsonify(result)
    return jsonify({"error": "Order not found"}), 404
