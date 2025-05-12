from models.product import Product
from enumerations.enums import ProductType
from app import db

def get_all_products():
    """Fetch all products from the database."""
    return Product.query.all()

def get_product_by_id(product_id):
    """Fetch a single product by ID."""
    return Product.query.get(product_id)

def get_products_by_store(store_id):
    """Fetch all products for a specific store."""
    return Product.query.filter_by(store_id=store_id).all()

def get_top3_products_by_store(store_id, limit=3):
    """Fetch top 3 products by score for a specific store"""
    return Product.query.filter_by(store_id=store_id).order_by(Product.score.desc()).limit(limit).all()

def create_product(store_id, name, product_type, unit_price, detail, score, image):
    """Create a new product."""
    new_product = Product(store_id, name, product_type, unit_price, detail, score, image)
    db.session.add(new_product)
    db.session.commit()
    return new_product

def update_product(product_id, store_id, name, product_type, unit_price, detail, score, image):
    """Update an existing product."""
    product = Product.query.get(product_id)
    if not product:
        return None  # Product not found

    product.store_id = store_id
    product.name = name
    product.product_type = ProductType(product_type)
    product.unit_price = unit_price
    product.detail = detail
    product.score = score
    product.image = image

    db.session.commit()
    return product

def delete_product(product_id):
    """Delete a product from the database."""
    product = Product.query.get(product_id)
    if not product:
        return None  # Product not found

    db.session.delete(product)
    db.session.commit()
    return {"message": f"Product {product_id} deleted successfully"}
