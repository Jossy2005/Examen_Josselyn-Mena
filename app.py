from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    """Endpoint de verificación de estado (Health Check)"""
    return jsonify({"message": "API funcionando correctamente"}), 200

# Endpoint "IA" (simple, simula procesamiento)
@app.route("/predict", methods=["POST"])
def predict():
    """Recibe un JSON con 'text' y devuelve una respuesta simulada"""
    try:
        data = request.get_json()

        # Validación básica
        if not data or "text" not in data:
            return jsonify({"error": "Debe enviar el campo 'text'"}), 400

        text = data["text"]

        # Lógica de IA mínima (procesamiento de texto)
        respuesta = f"IA procesó tu texto: {text}"

        return jsonify({"result": respuesta}), 200
        
    except Exception as e:
        return jsonify({"error": f"Ocurrió un error interno: {str(e)}"}), 500

if __name__ == "__main__":
    # host="0.0.0.0" es CRUCIAL para Docker
    app.run(host="0.0.0.0", port=5000)