from marshmallow import Schema, fields

class CartProductSchema(Schema):
    cart_id = fields.Int(required=True)  # Foreign key to Cart
    product_id = fields.Int(required=True)  # Foreign key to Product
