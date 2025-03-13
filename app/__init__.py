from flask import Flask
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from dotenv import load_dotenv
import os
from supabase import create_client, Client

load_dotenv()
# Create the Flask app
def create_app():

    app = Flask(__name__)
    SUPABASE_URL = os.getenv("SUPABASE_DB_URL")
    SUPABASE_KEY = os.getenv("SUPABASE_ANON_KEY")
    print("Supabase URL:", SUPABASE_URL)
    print("Supabase Key:", SUPABASE_KEY)
    supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)
    app.config["SUPABASE"] = supabase

    # Import and register blueprints
    from .routes import main
    app.register_blueprint(main)

    return app