from flask import Blueprint, jsonify, request
from services.product_service import *
from schemas.product_schema import ProductSchema

product_bp = Blueprint("product_bp", __name__)

# Initialize Schema
product_schema = ProductSchema()
products_schema = ProductSchema(many=True)

# ✅ GET all products
@product_bp.route("/", methods=["GET"])
def get_products():
    products_list = get_all_products()
    return jsonify(products_schema.dump(products_list))

# ✅ GET a product by ID
@product_bp.route("/<int:product_id>", methods=["GET"])
def get_product(product_id):
    product = get_product_by_id(product_id)
    if product:
        return jsonify(product_schema.dump(product))
    return jsonify({"error": "Product not found"}), 404

# ✅ GET products by store
@product_bp.route("/store/<int:store_id>", methods=["GET"])
def get_products_by_store_route(store_id):
    products = get_products_by_store(store_id)
    return jsonify(products_schema.dump(products))

# ✅ CREATE a new product
@product_bp.route("/", methods=["POST"])
def add_product():
    data = request.get_json()

    # Validate input
    errors = product_schema.validate(data)
    if errors:
        return jsonify({"error": errors}), 400

    new_product = create_product(
        data["store_id"], data["name"], data["product_type"], 
        data["unit_price"], data.get("detail"), data.get("score"), data["image"]
    )

    return jsonify(product_schema.dump(new_product)), 201

# ✅ UPDATE a product
@product_bp.route("/<int:product_id>", methods=["PUT"])
def modify_product(product_id):
    data = request.get_json()

    # Validate input
    errors = product_schema.validate(data)
    if errors:
        return jsonify({"error": errors}), 400

    updated_product = update_product(
        product_id, data["store_id"], data["name"], data["product_type"], 
        data["unit_price"], data.get("detail"), data.get("score"), data["image"]
    )

    if updated_product:
        return jsonify(product_schema.dump(updated_product))
    return jsonify({"error": "Product not found"}), 404

# ✅ DELETE a product
@product_bp.route("/<int:product_id>", methods=["DELETE"])
def remove_product(product_id):
    result = delete_product(product_id)
    if result:
        return jsonify(result)
    return jsonify({"error": "Product not found"}), 404

# ✅ GET top 3 products by store
@product_bp.route("/store/<int:store_id>/top3", methods=["GET"])
def get_top_products_by_store_route(store_id):
    products = get_top3_products_by_store(store_id)
    return jsonify(products_schema.dump(products))
