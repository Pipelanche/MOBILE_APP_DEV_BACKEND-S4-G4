from marshmallow import Schema, fields

class LocationSchema(Schema):
    
    location_id = fields.Int(dump_only=True)  # Auto-generated, so it's read-only
    latitude = fields.Float(required=True)  
    longitude = fields.Float(required=True)
    count = fields.Int(required=True)