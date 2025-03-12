from marshmallow import Schema, fields

class UserStoreSchema(Schema):
    user_id = fields.Int(required=True)  # Foreign key to User
    store_id = fields.Int(required=True)  # Foreign key to Store
