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

    # Import models here to ensure they are registered with SQLAlchemy
    from . import models

    # Add a simple route for the root URL to serve the index.html
    @app.route("/")
    def index():
        # Assuming index.html is in the static folder, but serving it via render_template
        # might be needed if you want to pass Flask variables to it later.
        # For a pure static SPA-like page, Flask serves static/index.html automatically
        # if no other route matches '/'. However, explicitly defining it is clearer.
        # If you want Flask to *just* serve static files, you might not need this route
        # depending on config, but it's good practice to have an index route.
        # Let's use send_from_directory for clarity with static files.
        from flask import send_from_directory

        # Serve from the 'static' folder in the 'app' directory
        return send_from_directory(app.static_folder, "index.html")

    # Shell context for flask shell
    @app.shell_context_processor
    def make_shell_context():
        # Add models and other useful variables to the shell context
        return {"db": db, "Character": models.Character, "Event": models.Event}

    return app
