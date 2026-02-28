import click
from .extensions import db
from .models import User

def register_commands(app):

    @app.cli.command("create-user")
    @click.argument("username")
    @click.argument("email")
    @click.argument("password")
    def create_user(username, email, password):
        """Create user from terminal"""

        if User.query.filter_by(email=email).first():
            #print("Email already exists!")
            return

        if User.query.filter_by(username=username).first():
            #print("Username already exists!")
            return

        user = User(username=username, email=email)
        user.set_password(password)   # ✅ uses your model method

        db.session.add(user)
        db.session.commit()

        #print(f"User '{username}' created successfully!")