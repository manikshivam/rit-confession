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
    
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAILTRAP_API_TOKEN=os.environ.get("MAILTRAP_API_TOKEN")
