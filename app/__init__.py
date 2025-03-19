from flask import Flask
from dotenv import load_dotenv
import os
from supabase import create_client, Client


load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_DB_URL")
SUPABASE_KEY = os.getenv("SUPABASE_ANON_KEY")

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

# Create the Flask app
def create_app():

    app = Flask(__name__)

    # Import and register blueprints
    from .routes import main
    from blueprints.feedback import feedback_bp

    app.register_blueprint(feedback_bp)
    app.register_blueprint(main)

    return app