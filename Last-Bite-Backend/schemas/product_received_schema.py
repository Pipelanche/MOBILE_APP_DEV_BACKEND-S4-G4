from marshmallow import Schema, fields, validate

class ProductReceived(Schema):

    image_id = fields.Int(dump_only=True)  # Auto-generated, so it's read-only
    image_string = fields.Str(required=True, validate=validate.Length(min=1,max=1000))