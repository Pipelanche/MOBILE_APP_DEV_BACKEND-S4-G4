from models.cart_product import CartProduct
from models.cart import Cart
from app import db
from enumerations.enums import Status

def get_products_in_cart(cart_id):
    """Fetch all products in a specific cart."""
    return CartProduct.query.filter_by(cart_id=cart_id).all()

def add_product_to_cart(cart_id, product_id, quantity=1):
    """Add a product to a cart or update its quantity if already in cart."""

    cart = Cart.query.get(cart_id)
    if not cart:
        return {"error": "Cart not found"}, 404

    if cart.status in [Status.BILLED.value, Status.PAYMENT_PROGRESS.value]:
        return {"error": "Cannot modify a cart that is BILLED or PAYMENT_PROGRESS"}, 403

    cart_product = CartProduct.query.filter_by(cart_id=cart_id, product_id=product_id).first()

    if cart_product:
        # ✅ Update quantity if product already exists
        cart_product.quantity += quantity
    else:
        # ✅ Add new product with specified quantity
        cart_product = CartProduct(cart_id=cart_id, product_id=product_id, quantity=quantity)
        db.session.add(cart_product)

    db.session.commit()
    return cart_product

def update_product_quantity(cart_id, product_id, quantity):
    """Update the quantity of a product in the cart."""
    
    cart = Cart.query.get(cart_id)
    if not cart:
        return {"error": "Cart not found"}, 404

    if cart.status in [Status.BILLED.value, Status.PAYMENT_PROGRESS.value]:
        return {"error": "Cannot modify a cart that is BILLED or PAYMENT_PROGRESS"}, 403

    cart_product = CartProduct.query.filter_by(cart_id=cart_id, product_id=product_id).first()
    
    if not cart_product:
        return {"error": "Product not found in cart"}, 404

    if quantity <= 0:
        # ✅ Remove product if quantity is set to 0
        db.session.delete(cart_product)
    else:
        # ✅ Update quantity
        cart_product.quantity = quantity

    db.session.commit()
    return {"message": f"Updated product {product_id} quantity to {quantity} in cart {cart_id}"}

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
