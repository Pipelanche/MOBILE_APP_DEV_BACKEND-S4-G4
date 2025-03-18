from app import db
from enumerations.enums import UserType  # Import UserType Enum
from sqlalchemy.dialects.postgresql import ENUM  # For better compatibility with PostgreSQL

class User(db.Model):
    __tablename__ = "user"

    user_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    user_email = db.Column(db.String(240), nullable=False, unique=True)
    mobile_number = db.Column(db.String(60), nullable=False)
    area_id = db.Column(db.Integer, db.ForeignKey("area.area_id"), nullable=False)
    verification_code = db.Column(db.Integer, nullable=False)

    # Using Enum for user_type
    user_type = db.Column(db.Enum(UserType, name="user_type_enum"), nullable=False)  # CUSTOMER, DELIVERY, STORE
    
    description = db.Column(db.String(240), nullable=True)  # Optional field

    # Relationship with Area
    area = db.relationship("Area", back_populates="users")

    #Relationship with store for users with type STORE
    stores = db.relationship("UserStore", back_populates="user", cascade="all, delete-orphan")

    #Relationship with the suscriptions
    subscriptions = db.relationship("UserSubscription", back_populates="user", cascade="all, delete-orphan")

    #Relationship with the user ratings
    ratings = db.relationship("UserRating", back_populates="user", cascade="all, delete-orphan")

    # Relationship with Cart
    carts = db.relationship("Cart", back_populates="user", cascade="all, delete-orphan")

    # Relationship with Order
    orders = db.relationship("Order", back_populates="user", cascade="all, delete-orphan") 

    def __init__(self, name, user_email, mobile_number, area_id, verification_code ,user_type, description=None):
        self.name = name
        self.user_email = user_email
        self.mobile_number = mobile_number
        self.area_id = area_id
        self.verification_code = verification_code
        self.user_type = UserType(user_type)  # Ensure input is a valid enum
        self.description = description
