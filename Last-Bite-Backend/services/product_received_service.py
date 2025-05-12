from models.product_received import ProductReceived
from app import db


def generate_product_received(image_string):

    new_product_received = ProductReceived(image_string=image_string)
    db.session.add(new_product_received)
    db.session.commit()
    return new_product_received

def get_received_products():
    """Fetch all Product Received records from the database."""
    return ProductReceived.query.all()