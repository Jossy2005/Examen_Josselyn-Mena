import json
from app import app

def test_home_page():
    """Verifica que la página principal responda 200 y contenga HTML."""
    client = app.test_client()
    response = client.get("/")

    assert response.status_code == 200
    assert b"<html>" in response.data
    assert b"Bienvenido a la API Interactiva" in response.data


def test_predict_ok():
    """Verifica que /predict funcione correctamente con texto válido."""
    client = app.test_client()
    data = {"text": "Hola mundo"}

    response = client.post(
        "/predict",
        data=json.dumps(data),
        content_type="application/json"
    )

    json_resp = response.get_json()

    assert response.status_code == 200
    assert "input" in json_resp
    assert "tipo_respuesta" in json_resp
    assert "confianza" in json_resp
    assert "resultado" in json_resp
    assert json_resp["input"] == "Hola mundo"


def test_predict_missing_text():
    """Verifica que cuando falta el campo 'text', devuelva error 400."""
    client = app.test_client()

    response = client.post(
        "/predict",
        data=json.dumps({}),  # sin 'text'
        content_type="application/json"
    )

    assert response.status_code == 400
    assert response.get_json()["error"] == "Debe enviar el campo 'text'"
