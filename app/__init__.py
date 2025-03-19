from flask import Flask

def create_app():
    app = Flask(__name__)

    from .routes import main  # Ensure this import exists
    app.register_blueprint(main)  # Register blueprint

    return app
