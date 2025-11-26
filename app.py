from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({"message": "API funcionando correctamente"}), 200

# Endpoint "IA" (simple, como el del zip)
@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()

    if not data or "text" not in data:
        return jsonify({"error": "Debe enviar el campo 'text'"}), 400

    text = data["text"]

    # IA mínima (similar al ZIP)
    respuesta = f"IA procesó tu texto: {text}"

    return jsonify({"result": respuesta}), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
