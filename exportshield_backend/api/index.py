import sys
import os

# Add the parent directory to the path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from src.main import app

# This is required for Vercel serverless functions
app = app
