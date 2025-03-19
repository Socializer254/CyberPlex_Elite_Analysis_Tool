from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'your_secret_key'
    
    # Register your blueprints or routes here
    from .routes import main
    app.register_blueprint(main)
    
    # Other initializations...
    
    return app

# Expose the app instance for import
app = create_app()
