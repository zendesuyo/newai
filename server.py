from flask import Flask, request, jsonify
import google.generativeai as genai
import os

app = Flask(__name__)
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))  # Ambil dari GitHub Secrets

@app.route("/generate", methods=["POST"])
def generate():
    data = request.json
    model = genai.GenerativeModel(data.get("model", "gemini-pro"))
    response = model.generate_content(data["prompt"])
    return jsonify({"response": response.text})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
