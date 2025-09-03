import sys
import os

# Make sure your project directory is in sys.path
project_home = '/home/Arifnka1411/mysite'   # <-- adjust if needed
if project_home not in sys.path:
    sys.path.insert(0, project_home)

# Set environment variable (optional, good practice)
os.environ['FLASK_APP'] = 'app.py'

# Import Flask app
from app import app as application
