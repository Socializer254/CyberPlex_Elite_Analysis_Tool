from app import create_app  # Ensure 'create_app' is defined in __init__.py

app = create_app()

if __name__ == "__main__":
    from waitress import serve
    print("Starting server on http://127.0.0.1:5000")
    serve(app, host="0.0.0.0", port=5000)
