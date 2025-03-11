from routes.zone_routes import zone_bp
from routes.area_routes import area_bp

def register_routes(app):
    app.register_blueprint(zone_bp, url_prefix="/api/zones")
    app.register_blueprint(area_bp, url_prefix="/api/areas")
