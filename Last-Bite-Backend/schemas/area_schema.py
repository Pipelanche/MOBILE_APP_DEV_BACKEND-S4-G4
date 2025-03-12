from marshmallow import Schema, fields
from schemas.user_schema import UserSchema  # Import UserSchema

class AreaSchema(Schema):
    area_id = fields.Int(dump_only=True)  # Auto-generated primary key
    area_name = fields.Str(required=True)
    zone_id = fields.Int(required=True)  # Foreign key to Zone
    
    # Nested relationship: A Zone can have multiple Users
    users = fields.Nested(UserSchema, many=True, dump_only=True)
