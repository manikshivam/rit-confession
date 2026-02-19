from flask import Flask,render_template
from .extensions import db, login_manager
from .auth.routes import auth_bp
from .posts.routes import posts_bp
from .games.routes import game
from .core.routes import core
from .models import User

def create_app():
    app = Flask(__name__)
    app.config.from_object("config.Config")

    db.init_app(app)
    login_manager.init_app(app)

    login_manager.login_view = "auth.login"

    app.register_blueprint(auth_bp)
    app.register_blueprint(posts_bp)
    app.register_blueprint(game)
    app.register_blueprint(core)
    
    with app.app_context():
        db.create_all()

    return app

    
