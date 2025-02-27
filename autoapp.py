import os
from dotenv import load_dotenv
from app import create_app

# Load variables from .env (like SECRET_KEY, DATABASE_URL)
load_dotenv()

# Create the Flask app using the factory pattern
app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
