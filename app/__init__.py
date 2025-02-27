import os
from flask import Flask
from .extensions import db, migrate
from .auth.routes import auth_bp
from .main.routes import main_bp

def create_app():
    app = Flask(__name__)

    # Load config from environment variables or use fallbacks
    app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY", "dev_key")
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL", "sqlite:///dev.db")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    # Initialize database and migration
    db.init_app(app)
    migrate.init_app(app, db)

    # Register blueprints (auth, main, etc.)
    app.register_blueprint(auth_bp, url_prefix="/auth")
    app.register_blueprint(main_bp)

    return app
