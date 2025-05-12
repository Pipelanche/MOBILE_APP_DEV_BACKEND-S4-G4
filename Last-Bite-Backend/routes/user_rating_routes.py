from flask import Blueprint, jsonify, request
from services.user_rating_service import *
from schemas.user_rating_schema import UserRatingSchema

rating_bp = Blueprint("rating_bp", __name__)

# Initialize Schema
rating_schema = UserRatingSchema()
ratings_schema = UserRatingSchema(many=True)

# ✅ GET all ratings
@rating_bp.route("/", methods=["GET"])
def get_ratings():
    ratings_list = get_all_ratings()
    return jsonify(ratings_schema.dump(ratings_list))

# ✅ GET ratings by product
@rating_bp.route("/product/<int:product_id>", methods=["GET"])
def get_ratings_by_product_route(product_id):
    ratings = get_ratings_by_product(product_id)
    return jsonify(ratings_schema.dump(ratings))

# ✅ GET ratings by user
@rating_bp.route("/user/<int:user_id>", methods=["GET"])
def get_ratings_by_user_route(user_id):
    ratings = get_ratings_by_user(user_id)
    return jsonify(ratings_schema.dump(ratings))

# ✅ GET a rating by ID
@rating_bp.route("/<int:rating_id>", methods=["GET"])
def get_rating(rating_id):
    rating = get_rating_by_id(rating_id)
    if rating:
        return jsonify(rating_schema.dump(rating))
    return jsonify({"error": "Rating not found"}), 404

# ✅ CREATE a new rating
@rating_bp.route("/", methods=["POST"])
def add_rating():
    data = request.get_json()

    # Validate input
    errors = rating_schema.validate(data)
    if errors:
        return jsonify({"error": errors}), 400

    new_rating = create_user_rating(data["product_id"], data["user_id"], data["score"])
    
    if isinstance(new_rating, dict):  # Check if it returned an error
        return jsonify(new_rating), 400

    return jsonify(rating_schema.dump(new_rating)), 201

# ✅ UPDATE a rating
@rating_bp.route("/<int:rating_id>", methods=["PUT"])
def modify_rating(rating_id):
    data = request.get_json()

    # Validate input
    errors = rating_schema.validate(data)
    if errors:
        return jsonify({"error": errors}), 400

    updated_rating = update_user_rating(rating_id, data["score"])
    if updated_rating:
        return jsonify(rating_schema.dump(updated_rating))
    return jsonify({"error": "Rating not found"}), 404

# ✅ DELETE a rating
@rating_bp.route("/<int:rating_id>", methods=["DELETE"])
def remove_rating(rating_id):
    result = delete_user_rating(rating_id)
    if result:
        return jsonify(result)
    return jsonify({"error": "Rating not found"}), 404
