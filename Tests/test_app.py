import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.main import app

def test_home():
    response = app.test_client().get('/')
    assert response.data == b"Hello, CI/CD World!"
