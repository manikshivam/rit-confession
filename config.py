import os
from dotenv import load_dotenv
from sqlalchemy.dialects.postgresql import base as pg_base

# LOAD ENV FIRST (VERY IMPORTANT)
load_dotenv()

# FIX COCKROACH VERSION ISSUE
pg_base.PGDialect._get_server_version_info = lambda self, connection: (15, 0)


class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "supersecretkey")

    # DATABASE
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # MAIL CONFIG
    MAIL_SERVER = os.getenv("MAIL_SERVER")
    MAIL_PORT = int(os.getenv("MAIL_PORT", 587))
    MAIL_USE_TLS = os.getenv("MAIL_USE_TLS", "True") == "True"
    MAIL_USERNAME = os.getenv("MAIL_USERNAME")
    MAIL_PASSWORD = os.getenv("MAIL_PASSWORD")
    MAIL_DEFAULT_SENDER = os.getenv("MAIL_DEFAULT_SENDER")