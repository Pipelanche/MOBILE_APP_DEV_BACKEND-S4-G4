from marshmallow import Schema, fields, validate
from enumerations.enums import ProductType

class ProductSchema(Schema):
    product_id = fields.Int(dump_only=True)  # Auto-generated ID
    store_id = fields.Int(required=True)  # Foreign key to Store
    name = fields.Str(required=True, validate=validate.Length(min=1,max=150))
    product_type = fields.Str(required=True, validate=validate.OneOf([t.value for t in ProductType]))  # Enum validation
    unit_price = fields.Float(required=True)
    detail = fields.Str(validate=validate.Length(max=240))
    score = fields.Float()
    image = fields.Str(required=True, validate=validate.Length(min=1, max=1000))
