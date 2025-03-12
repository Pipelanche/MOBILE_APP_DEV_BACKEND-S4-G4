from app import db

class UserStore(db.Model):
    __tablename__ = "user_store"

    user_id = db.Column(db.Integer, db.ForeignKey("user.user_id"), primary_key=True, nullable=False)
    store_id = db.Column(db.Integer, db.ForeignKey("store.store_id"), primary_key=True, nullable=False)

    # Relationships
    user = db.relationship("User", back_populates="stores")
    store = db.relationship("Store", back_populates="users")

    def __init__(self, user_id, store_id):
        self.user_id = user_id
        self.store_id = store_id
