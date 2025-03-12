from marshmallow import Schema, fields, validate

class StoreSchema(Schema):
    store_id = fields.Int(dump_only=True)  # Auto-generated ID
    nit = fields.Str(required=True, validate=validate.Length(min = 10,max=150))
    name = fields.Str(required=True, validate=validate.Length(min = 1,max=150))
    address = fields.Str(required=True, validate=validate.Length(min = 1,max=240))
    longitude = fields.Float(required=True)
    latitude = fields.Float(required=True)
    logo = fields.Str(required=True, validate=validate.Length(min = 1,max=1000))