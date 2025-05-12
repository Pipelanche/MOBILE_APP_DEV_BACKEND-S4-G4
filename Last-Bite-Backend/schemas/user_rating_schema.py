from marshmallow import Schema, fields, validate

class UserRatingSchema(Schema):
    rating_id = fields.Int(dump_only=True)  # Auto-generated primary key
    product_id = fields.Int(required=True)  # Foreign key to Product
    user_id = fields.Int(required=True)  # Foreign key to User
    score = fields.Int(required=True, validate=validate.Range(min=1, max=5))  # Score between 1 and 5
