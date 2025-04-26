from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from config import app_config
from flask_migrate import Migrate

# Initialize the app
app = Flask(__name__)
app.config.from_object(app_config)

# Initialize extensions
db = SQLAlchemy(app)
CORS(app)
migrate = Migrate(app, db)  # Flask-Migrate

# Import models here to make sure they are registered
from models.zone import Zone
from models.signup_events import SignupEvent

# Import routes
from routes import register_routes
register_routes(app)

if __name__ == "__main__":
    app.run(debug=True)
