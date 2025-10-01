import sys, os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

import pytest
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_home(client):
    res = client.get("/")
    assert res.status_code == 200
    assert res.get_json() == {"message": "Hola, mundo desde Flask con GitHub Actions!"}
    
def test_secret(client):
    res = client.get("/secret")
    assert res.status_code == 200
    assert res.get_json() == {"secret": os.getenv("MY_SECRET", "No se encontró el secret")}