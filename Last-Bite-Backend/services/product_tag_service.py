from models.product_tag import ProductTag
from app import db

MAX_TAGS_PER_PRODUCT = 5

def get_all_tags():
    """Fetch all product tags from the database."""
    return ProductTag.query.all()

def get_tags_by_product(product_id):
    """Fetch all tags for a specific product."""
    return ProductTag.query.filter_by(product_id=product_id).all()

def get_tag_by_id(product_tag_id):
    """Fetch a single tag by ID."""
    return ProductTag.query.get(product_tag_id)

def create_product_tag(product_id, value):
    """Create a new product tag, ensuring no more than 5 tags per product."""
    
    tag_count = ProductTag.query.filter_by(product_id=product_id).count()
    
    if tag_count >= MAX_TAGS_PER_PRODUCT:
        return {"error": f"A product can have a maximum of {MAX_TAGS_PER_PRODUCT} tags"}, 400  # HTTP 400 Bad Request

    # Create and save the new tag
    new_tag = ProductTag(product_id, value)
    db.session.add(new_tag)
    db.session.commit()
    return new_tag

def update_product_tag(product_tag_id, value):
    """Update an existing product tag."""
    tag = ProductTag.query.get(product_tag_id)
    if not tag:
        return None  # Tag not found

    tag.value = value
    db.session.commit()
    return tag

def delete_product_tag(product_tag_id):
    """Delete a product tag from the database."""
    tag = ProductTag.query.get(product_tag_id)
    if not tag:
        return None  # Tag not found

    db.session.delete(tag)
    db.session.commit()
    return {"message": f"Tag {product_tag_id} deleted successfully"}
