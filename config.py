import os
from dotenv import load_dotenv

load_dotenv()  # local only

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "supersecretkey")

    DB_URL = os.getenv("DATABASE_URL")

    # Fix Render/Supabase postgres format
    if DB_URL and DB_URL.startswith("postgres://"):
        DB_URL = DB_URL.replace("postgres://", "postgresql://", 1)

    SQLALCHEMY_DATABASE_URI = DB_URL or "sqlite:///site.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False