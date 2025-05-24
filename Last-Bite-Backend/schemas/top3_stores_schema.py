from marshmallow import Schema, fields

class Top3StoresSchema(Schema):

    top_3_stores_id = fields.Int(dump_only=True)  # Auto-generated, so it's read-only
    store1_name = fields.Str(required=True)
    store2_name = fields.Str(required=True) 
    store3_name = fields.Str(required=True) 