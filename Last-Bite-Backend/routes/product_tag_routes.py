from flask import Blueprint, jsonify, request
from services.product_tag_service import *
from schemas.product_tag_schema import ProductTagSchema

tag_bp = Blueprint("tag_bp", __name__)

# Initialize Schema
tag_schema = ProductTagSchema()
tags_schema = ProductTagSchema(many=True)

# ✅ GET all tags
@tag_bp.route("/", methods=["GET"])
def get_tags():
    tags_list = get_all_tags()
    return jsonify(tags_schema.dump(tags_list))

# ✅ GET tags by product
@tag_bp.route("/product/<int:product_id>", methods=["GET"])
def get_tags_by_product_route(product_id):
    tags = get_tags_by_product(product_id)
    return jsonify(tags_schema.dump(tags))

# ✅ GET a tag by ID
@tag_bp.route("/<int:product_tag_id>", methods=["GET"])
def get_tag(product_tag_id):
    tag = get_tag_by_id(product_tag_id)
    if tag:
        return jsonify(tag_schema.dump(tag))
    return jsonify({"error": "Tag not found"}), 404

# ✅ CREATE a new product tag
@tag_bp.route("/", methods=["POST"])
def add_tag():
    data = request.get_json()

    # Validate input
    errors = tag_schema.validate(data)
    if errors:
        return jsonify({"error": errors}), 400

    new_tag = create_product_tag(data["product_id"], data["value"])
    return jsonify(tag_schema.dump(new_tag)), 201

# ✅ UPDATE a product tag
@tag_bp.route("/<int:product_tag_id>", methods=["PUT"])
def modify_tag(product_tag_id):
    data = request.get_json()

    # Validate input
    errors = tag_schema.validate(data)
    if errors:
        return jsonify({"error": errors}), 400

    updated_tag = update_product_tag(product_tag_id, data["value"])
    if updated_tag:
        return jsonify(tag_schema.dump(updated_tag))
    return jsonify({"error": "Tag not found"}), 404

# ✅ DELETE a product tag
@tag_bp.route("/<int:product_tag_id>", methods=["DELETE"])
def remove_tag(product_tag_id):
    result = delete_product_tag(product_tag_id)
    if result:
        return jsonify(result)
    return jsonify({"error": "Tag not found"}), 404
