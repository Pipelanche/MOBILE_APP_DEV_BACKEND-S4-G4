from routes.user_routes import user_bp
from routes.zone_routes import zone_bp
from routes.area_routes import area_bp
from routes.store_routes import store_bp
from routes.user_store_routes import user_store_bp
from routes.product_routes import product_bp

def register_routes(app):
    app.register_blueprint(user_bp, url_prefix="/api/users")
    app.register_blueprint(zone_bp, url_prefix="/api/zones")
    app.register_blueprint(area_bp, url_prefix="/api/areas")
    app.register_blueprint(store_bp, url_prefix="/api/stores")
    app.register_blueprint(user_store_bp, url_prefix="/api/user_store")
    app.register_blueprint(product_bp, url_prefix="/api/products")
