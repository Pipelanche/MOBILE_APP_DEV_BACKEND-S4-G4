from marshmallow import Schema, fields, validate

class ProductTagSchema(Schema):
    product_tag_id = fields.Int(dump_only=True)  # Auto-generated primary key
    product_id = fields.Int(required=True)  # Foreign key to Product
    value = fields.Str(required=True, validate=validate.Length(min=1, max=30))  # Min 1 char, max 30 chars
