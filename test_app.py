from app import app

# Crear un cliente de pruebas
client = app.test_client()

def test_home_status_code():
    """Verifica que la ruta principal responde 200 OK"""
    response = client.get("/")
    assert response.status_code == 200
    print("test_home_status_code: OK")

def test_home_content():
    """Verifica que el contenido de la ruta principal tenga algo"""
    response = client.get("/")
    if b"Hola" in response.data or b"hello" in response.data or response.data != b"":
        print("test_home_content: OK")
    else:
        print("test_home_content: FAIL")

def test_not_found():
    """Verifica que rutas no existentes devuelvan 404"""
    response = client.get("/ruta_que_no_existe")
    assert response.status_code == 404
    print("test_not_found: OK")

if __name__ == "__main__":
    test_home_status_code()
    test_home_content()
    test_not_found()
