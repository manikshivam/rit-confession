# import os

# class Config:
#     SECRET_KEY = "supersecretkey"
#     SQLALCHEMY_DATABASE_URI = "sqlite:///site.db"
#     SQLALCHEMY_TRACK_MODIFICATIONS = False
import os
from dotenv import load_dotenv

class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY", "supersecretkey")
    
    load_dotenv()

# Neon/PostgreSQL connection
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    
    MAIL_SERVER = os.getenv("MAIL_SERVER")
    MAIL_PORT = int(os.getenv("MAIL_PORT", 587))
    MAIL_USE_TLS = os.getenv("MAIL_USE_TLS", "True") == "True"
    MAIL_USERNAME = os.getenv("MAIL_USERNAME")
    MAIL_PASSWORD = os.getenv("MAIL_PASSWORD")
    MAIL_DEFAULT_SENDER = os.getenv("MAIL_DEFAULT_SENDER")
