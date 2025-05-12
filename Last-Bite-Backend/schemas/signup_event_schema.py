from marshmallow import Schema, fields, validate

class SignupEventSchema(Schema):
    attempt_id   = fields.UUID(required=True, description="UUID generado por el cliente para el intento")
    user_id      = fields.UUID(allow_none=True, description="UUID del usuario registrado, una vez completado")
    started_at   = fields.DateTime(required=True, description="Timestamp UTC de inicio del intento")
    completed_at = fields.DateTime(allow_none=True, description="Timestamp UTC de finalización, si existe")
    status       = fields.Str(required=True, validate=validate.OneOf(["started", "completed"]), description="Estado del intento")