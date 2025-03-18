from marshmallow import Schema, fields, validate
from enumerations.enums import Status

class CartSchema(Schema):
    cart_id = fields.Int(dump_only=True)  # Auto-generated primary key
    user_id = fields.Int(required=True)  # Foreign key to User
    creation_date = fields.Date(dump_only=True)  # Auto-generated
    status = fields.Str(required=True, validate=validate.OneOf([s.value for s in Status]))  # Validate enum
    status_date = fields.Date(dump_only=True)  # ✅ Now it's optional (auto-generated)
