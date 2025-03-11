from marshmallow import Schema, fields
from schemas.area_schema import AreaSchema  # Import AreaSchema

class ZoneSchema(Schema):
    zone_id = fields.Int(dump_only=True)  # Auto-generated, so it's read-only
    zone_name = fields.Str(required=True)

    # Nested relationship: A Zone can have multiple Areas
    areas = fields.Nested(AreaSchema, many=True, dump_only=True)