from models.cart_product import CartProduct
from models.cart import Cart
from app import db
from enumerations.enums import Status

def get_products_in_cart(cart_id):
    """Fetch all products in a specific cart."""
    return CartProduct.query.filter_by(cart_id=cart_id).all()

def add_product_to_cart(cart_id, product_id):
    """Add a product to a cart if it's not BILLED or PAYMENT_PROGRESS."""
    
    cart = Cart.query.get(cart_id)
    if not cart:
        return {"error": "Cart not found"}, 404

    if cart.status in [Status.BILLED.value, Status.PAYMENT_PROGRESS.value]:
        return {"error": "Cannot modify a cart that is BILLED or PAYMENT_PROGRESS"}, 403

    existing_product = CartProduct.query.filter_by(cart_id=cart_id, product_id=product_id).first()
    if existing_product:
        return {"error": "Product is already in the cart"}, 409  # Conflict

    new_cart_product = CartProduct(cart_id, product_id)
    db.session.add(new_cart_product)
    db.session.commit()
    return new_cart_product

def remove_product_from_cart(cart_id, product_id):
    """Remove a product from a cart if it's not BILLED or PAYMENT_PROGRESS."""
    
    cart = Cart.query.get(cart_id)
    if not cart:
        return {"error": "Cart not found"}, 404

    if cart.status in [Status.BILLED.value, Status.PAYMENT_PROGRESS.value]:
        return {"error": "Cannot remove products from a cart that is BILLED or PAYMENT_PROGRESS"}, 403

    cart_product = CartProduct.query.filter_by(cart_id=cart_id, product_id=product_id).first()
    if not cart_product:
        return {"error": "Product not found in cart"}, 404

    db.session.delete(cart_product)
    db.session.commit()
    return {"message": f"Product {product_id} removed from cart {cart_id} successfully"}
