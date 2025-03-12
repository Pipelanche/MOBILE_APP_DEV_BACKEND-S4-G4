from marshmallow import Schema, fields, validate
from enumerations.enums import UserType  # Import UserType Enum

class UserSchema(Schema):
    user_id = fields.Int(dump_only=True)  # Auto-generated primary key
    name = fields.Str(required=True, validate=validate.Length(min=1,max=150))
    user_email = fields.Email(required=True, validate=validate.Length(max=240))
    mobile_number = fields.Str(required=True, validate=validate.Length(min=1,max=60))
    area_id = fields.Int(required=True)  # Foreign Key
    verification_code = fields.Int(required=True)

    # Enum validation for user_type
    user_type = fields.Str(required=True, validate=validate.OneOf([e.value for e in UserType]))

    description = fields.Str(validate=validate.Length(max=240), allow_none=True)
