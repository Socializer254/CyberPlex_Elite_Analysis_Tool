import os
from app import app  # Ensure 'app' is properly imported

port = int(os.environ.get("PORT", 5000))  # Use the PORT variable from Render
app.run(debug=True, host="0.0.0.0", port=port)
