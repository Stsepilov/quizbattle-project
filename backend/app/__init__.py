import os

from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

db = SQLAlchemy()
migrate = Migrate()


def create_app(test_config=None):
    app = Flask(__name__)
    CORS(app)
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    if test_config:
        app.config.update(test_config)
    else:
        app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("DATABASE_URL")

    db.init_app(app)
    migrate.init_app(app, db)

    # Импортируем и регистрируем маршруты
    from .routes import bp as routes_bp
    app.register_blueprint(routes_bp)

    return app
