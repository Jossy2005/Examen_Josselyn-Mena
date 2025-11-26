import json
from app import app

def test_home():
    tester = app.test_client()
    response = tester.get("/")
    assert response.status_code == 200
    assert b"API funcionando" in response.data

def test_predict_ok():
    tester = app.test_client()
    response = tester.post(
        "/predict",
        data=json.dumps({"text": "hola"}),
        content_type="application/json"
    )
    assert response.status_code == 200
    json_data = json.loads(response.data)
    assert "IA procesó tu texto" in json_data["result"]

def test_predict_error():
    tester = app.test_client()
    response = tester.post(
        "/predict",
        data=json.dumps({}),   # falta "text"
        content_type="application/json"
    )
    assert response.status_code == 400
