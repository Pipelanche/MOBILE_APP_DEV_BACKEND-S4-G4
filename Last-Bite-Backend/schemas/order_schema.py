from marshmallow import Schema, fields, validate
from enumerations.enums import Status

class OrderSchema(Schema):
    order_id = fields.Int(dump_only=True)  # Auto-generated primary key
    user_id = fields.Int(required=True)  # Foreign key to User
    cart_id = fields.Int(required=True)  # Foreign key to Cart
    creation_date = fields.Date(dump_only=True)  # Auto-generated
    status = fields.Str(required=True, validate=validate.OneOf([s.value for s in Status]))  # Validate enum
    billed_date = fields.Date(required=False)  # Optional
    total_price = fields.Float(required=True)  # Total price

# ✅ Schema for updates (only requires `order_id`, `status`, `total_price`)
class OrderUpdateSchema(Schema):
    status = fields.Str(required=True, validate=validate.OneOf([s.value for s in Status]))
    total_price = fields.Float(required=True)
