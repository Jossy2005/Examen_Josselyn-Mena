from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "¡Hola, mundo! Bienvenido a Flask."

# --- Tests simples usando solo Flask ---
def run_tests():
    print("Ejecutando tests...")
    client = app.test_client()

    # Test 1: Status code de la ruta principal
    response = client.get("/")
    assert response.status_code == 200
    print("✅ test_home_status_code: OK")

    # Test 2: Contenido de la ruta principal
    response = client.get("/")
    assert b"Hola" in response.data
    print("✅ test_home_content: OK")

    # Test 3: Ruta no encontrada devuelve 404
    response = client.get("/ruta_que_no_existe")
    assert response.status_code == 404
    print("✅ test_not_found: OK")

# --- Ejecutar app o tests según el modo ---
if __name__ == "__main__":
    import sys
    if "test" in sys.argv:
        run_tests()
    else:
        app.run(host="0.0.0.0", port=5000, debug=True)
