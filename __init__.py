from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from hashlib import md5
from datetime import timedelta
from flask_marshmallow import Marshmallow, fields


db = SQLAlchemy()
ma = Marshmallow()


def create_app():
    app = Flask(__name__)
    encryptor = md5()

    app.permanent_session_lifetime = timedelta(minutes=30)
    app.secret_key = encryptor.digest()
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
    db.init_app(app)
    ma.init_app(app)

    app.debug = True

    from .main import add_movie_blueprint, delete_movie_blueprint, get_movies_blueprint, get_movies_with_opinions_blueprint, index_blueprint

    app.register_blueprint(add_movie_blueprint)
    app.register_blueprint(delete_movie_blueprint)
    app.register_blueprint(get_movies_blueprint)
    app.register_blueprint(get_movies_with_opinions_blueprint)
    app.register_blueprint(index_blueprint)

    return app
