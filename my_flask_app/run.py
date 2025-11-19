import os
from app import create_app
from waitress import serve
from app.config import Config 
# Ensure working directory is where the exe is located
os.chdir(os.path.dirname(os.path.abspath(__file__)))

app = create_app()

if __name__ == "__main__":
    serve(app, host="0.0.0.0", port=int(Config.PORT))
