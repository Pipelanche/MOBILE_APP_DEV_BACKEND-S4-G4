from marshmallow import Schema, fields, validate
from enumerations.enums import SubscriptionType

class UserSubscriptionSchema(Schema):
    subscription_id = fields.Int(dump_only=True)  # Auto-generated ID
    product_id = fields.Int(required=True)  # Foreign key to Product
    user_id = fields.Int(required=True)  # Foreign key to User
    subscription_type = fields.Str(required=True, validate=validate.OneOf([t.value for t in SubscriptionType]))  # Enum validation
    start_date = fields.Date(required=True)  # Must be a valid date
    end_date = fields.Date(required=True)  # Must be a valid date
