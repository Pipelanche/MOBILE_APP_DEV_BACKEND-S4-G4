from app import db

class ProductReceived(db.Model):
    __tablename__ = "product_received"

    image_id = db.Column(db.Integer, primary_key=True)
    image_string = db.Column(db.String, nullable=False)

    def __init__(self, image_string):
        
        self.image_string = image_string