from routes.zone_routes import zone_bp

def register_routes(app):
    app.register_blueprint(zone_bp, url_prefix="/api/zones")
