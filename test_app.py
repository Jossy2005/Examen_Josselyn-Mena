import pytest
from app import app

@pytest.fixture
def client():
    """Configura el cliente de pruebas de Flask"""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home(client):
    """Prueba que el endpoint '/' responda correctamente"""
    response = client.get('/')
    assert response.status_code == 200
    assert response.json == {"message": "API funcionando correctamente"}

def test_predict_success(client):
    """Prueba que '/predict' funcione con datos válidos"""
    test_data = {"text": "Hola mundo"}
    response = client.post('/predict', json=test_data)
    
    assert response.status_code == 200
    assert "result" in response.json
    assert response.json["result"] == "IA procesó tu texto: Hola mundo"

def test_predict_missing_field(client):
    """Prueba que '/predict' devuelva error 400 si falta el campo 'text'"""
    test_data = {"otro_campo": "valor"}
    response = client.post('/predict', json=test_data)
    
    assert response.status_code == 400
    assert "error" in response.json
    assert response.json["error"] == "Debe enviar el campo 'text'"

def test_predict_empty_json(client):
    """Prueba que '/predict' maneje JSON vacío"""
    response = client.post('/predict', json={})
    assert response.status_code == 400