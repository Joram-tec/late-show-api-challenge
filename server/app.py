from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from dotenv import load_dotenv
from pathlib import Path
import os


load_dotenv(dotenv_path=Path(__file__).resolve().parent / ".env")

from config import Config
from server.extensions import db, migrate, jwt

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app,db)
    jwt.init_app(app)

    from server.models.guest import Guest
    from server.models.episode import Episode
    from server.models.appearance import Appearance

    from server.controllers.auth_controller import auth_blues
    from server.controllers.guest_controller import guest_blues
    from server.controllers.appearance_controller import appearance_blues
    from server.controllers.episode_controller import episode_blues

    app.register_blueprint(auth_blues,url_prefix="/auth")
    app.register_blueprint(guest_blues, url_prefix="/guests")
    app.register_blueprint(appearance_blues, url_prefix="/appearances")
    app.register_blueprint(episode_blues,url_prefix="/episodes")

    @app.route('/')
    def home():
        return {'message': 'Welcome to the Late Show API!'}

    return app

app = create_app()

if __name__ == "__main__":
    app.run(port=5555, debug=True)
