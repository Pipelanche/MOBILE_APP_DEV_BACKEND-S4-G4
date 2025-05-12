from app import db

class StoreCount(db.Model):
    __tablename__ = "store_count"

    store_count_id = db.Column(db.Integer, primary_key=True)
    store_id = db.Column(db.Integer, db.ForeignKey("store.store_id"), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("user.user_id"), nullable=False)
    count = db.Column(db.Integer, nullable=False)

    # Relationship with Store
    # store = db.relationship("Store", back_populates="count")
    # Relationship with User
    # user = db.relationship("User", back_populates="store_count")

    def __init__(self, store_id, user_id):

        self.store_id = store_id
        self.user_id = user_id
        self.count = 1