from marshmallow import Schema, fields

class AreaSchema(Schema):
    area_id = fields.Int(dump_only=True)  # Auto-generated primary key
    area_name = fields.Str(required=True)
    zone_id = fields.Int(required=True)  # Foreign key to Zone
