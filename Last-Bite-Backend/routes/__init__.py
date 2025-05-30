from routes.user_routes import user_bp
from routes.zone_routes import zone_bp
from routes.area_routes import area_bp
from routes.store_routes import store_bp
from routes.user_store_routes import user_store_bp
from routes.product_routes import product_bp
from routes.user_subscription_routes import subscription_bp
from routes.product_tag_routes import tag_bp
from routes.user_rating_routes import rating_bp
from routes.cart_routes import cart_bp
from routes.cart_product_routes import cart_product_bp
from routes.order_routes import order_bp
from routes.location_routes import location_bp
from routes.product_received_routes import product_received_bp
from routes.store_count_routes import store_count_bp

def register_routes(app):
    app.register_blueprint(user_bp, url_prefix="/api/users")
    app.register_blueprint(zone_bp, url_prefix="/api/zones")
    app.register_blueprint(area_bp, url_prefix="/api/areas")
    app.register_blueprint(store_bp, url_prefix="/api/stores")
    app.register_blueprint(user_store_bp, url_prefix="/api/user_store")
    app.register_blueprint(product_bp, url_prefix="/api/products")
    app.register_blueprint(subscription_bp, url_prefix="/api/user_subscriptions")
    app.register_blueprint(tag_bp, url_prefix="/api/tags")
    app.register_blueprint(rating_bp, url_prefix="/api/ratings")
    app.register_blueprint(cart_bp, url_prefix="/api/carts")
    app.register_blueprint(cart_product_bp, url_prefix="/api/cart_products")
    app.register_blueprint(order_bp, url_prefix="/api/orders")
    app.register_blueprint(location_bp, url_prefix="/api/location")
    app.register_blueprint(product_received_bp, url_prefix="/api/product_received")
    app.register_blueprint(store_count_bp, url_prefix="/api/store_counted")
