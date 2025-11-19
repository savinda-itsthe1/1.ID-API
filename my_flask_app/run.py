import os
from app import create_app
from waitress import serve

# Ensure working directory is where the exe is located
os.chdir(os.path.dirname(os.path.abspath(__file__)))

app = create_app()

if __name__ == "__main__":
    serve(app, host="0.0.0.0", port=5000)
