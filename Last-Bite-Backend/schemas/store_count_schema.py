from marshmallow import Schema, fields

class StoreCountSchema(Schema):

    count_store_id = fields.Int(dump_only=True)  # Auto-generated, so it's read-only
    store_id = fields.Int(required=True) # Foreign key to Store
    user_id = fields.Int(required=True) # Foreign key to User
    count = fields.Int(required=True)