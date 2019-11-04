import firebase_admin
from flask import Flask
from flask_cors import CORS

from src.adapters.controllers.library_controller import library
from src.adapters.controllers.pronunciation_controller import pronunciation
from src.adapters.controllers.recommended_controller import recommended
from src.adapters.controllers.song_controller import song
from src.adapters.controllers.trending_controller import trending

config = {"development": "config.DevelopmentConfig", "production": "config.ProductionConfig"}

secrets = "secrets.Secrets"

origins = ["http://localhost:8080/*", "https://parrot-n2zzz72gsq-uc.a.run.app/*"]


def create_app() -> Flask:
    app = Flask(__name__)
    app.config.from_object(config[app.config.get("ENV", "development")])
    app.config.from_object(secrets)

    firebase_admin.initialize_app()

    app.register_blueprint(library)
    app.register_blueprint(pronunciation)
    app.register_blueprint(recommended)
    app.register_blueprint(song)
    app.register_blueprint(trending)

    CORS(app, origins=origins)

    return app
