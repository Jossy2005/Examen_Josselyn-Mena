from flask import Flask, request, jsonify, render_template_string
import random
import datetime

app = Flask(__name__)

# ----------------------------
# Página principal (HTML simple)
# ----------------------------
@app.route("/")
def home():
    html = """
    <html>
        <head>
            <title>API Interactiva</title>
        </head>
        <body style="font-family: Arial; padding: 40px;">
            <h1>🚀 Bienvenido a la API Interactiva</h1>
            <p>Usa el endpoint <strong>/predict</strong> enviando JSON para recibir una respuesta IA simulada.</p>
            <p>Ejemplo:</p>
            <pre>
POST /predict
Content-Type: application/json

{
    "text": "hola mundo"
}
            </pre>
        </body>
    </html>
    """
    return render_template_string(html)


# ----------------------------
# Endpoint de "IA" más interactivo
# ----------------------------
@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()

    if not data or "text" not in data:
        return jsonify({"error": "Debe enviar el campo 'text'"}), 400

    text = data["text"]

    # Simulamos un análisis más interactivo
    confidence = round(random.uniform(0.60, 0.99), 2)
    tipo = random.choice(["análisis general", "clasificación básica", "respuesta creativa"])

    respuesta = f"Procesé tu texto y aquí está el resultado 😉"

    # Log en consola (útil para debug)
    print(f"[{datetime.datetime.now()}] Texto recibido: {text}")

    return jsonify({
        "input": text,
        "tipo_respuesta": tipo,
        "confianza": confidence,
        "resultado": f"IA procesó tu texto: {text}"
    }), 200


# ----------------------------
# Iniciar servidor Flask
# ----------------------------
if __name__ == "__main__":
    print("🚀 Servidor iniciando en http://0.0.0.0:5000 ...")
    app.run(host="0.0.0.0", port=5000)
