from flask import Flask
from config import Config
from .extensions import db, migrate


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initialize Flask extensions here
    db.init_app(app)
    migrate.init_app(app, db)

    # Register blueprints here
    from .api import bp as api_bp

    app.register_blueprint(api_bp)

    # Create database tables if they don't exist
    with app.app_context():
        db.create_all()

    return app
