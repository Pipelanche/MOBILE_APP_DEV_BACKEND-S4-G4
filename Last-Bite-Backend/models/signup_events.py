import uuid
from datetime import datetime, timezone
from app import db

class SignupEvent(db.Model):
    __tablename__ = 'signup_events'
    attempt_id = db.Column(db.Integer, primary_key=True)
    user_id      = db.Column(db.String(36), db.ForeignKey('user.user_id'), nullable=True)
    started_at   = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    completed_at = db.Column(db.DateTime, nullable=True)
    status       = db.Column(db.String(20), default='started', nullable=False)