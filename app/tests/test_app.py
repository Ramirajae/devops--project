import pytest
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from app import app as flask_app

@pytest.fixture
def client():
    flask_app.config['TESTING'] = True
    with flask_app.test_client() as client:
        yield client

def test_home(client):
    res = client.get('/')
    assert res.status_code == 200

def test_health(client):
    res = client.get('/health')
    assert res.status_code == 200
