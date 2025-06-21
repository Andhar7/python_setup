import os

from dotenv import load_dotenv

from setup import check_out

load_dotenv

DATABASE_URL = os.getenv("DATABASE_URL")
SECRET_KEY = os.getenv("SECRET_KEY")

check_out()