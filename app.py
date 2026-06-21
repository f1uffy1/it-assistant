import requests
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

OLLAMA = "http://localhost:11434/api/generate"

system_ctx = """You are an IT support technician. When someone describes a problem:
- acknowledge it briefly
- give practical step by step fixes
- mention when they should escalate
Keep it short and dont use a lot of jargon."""

def ask_model(user_input):
    payload = {
        "model": "mistral",
        "prompt": f"{system_ctx}\n\nissue: {user_input}",
        "stream": False
    }
    try:
        r = requests.post(OLLAMA, json=payload, timeout=120)
        return r.json()["response"].strip()
    except Exception as e:
        return f"something went wrong: {e}"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask():
    msg = request.get_json().get("message", "")
    if not msg:
        return jsonify({"error": "empty message"}), 400
    return jsonify({"response": ask_model(msg)})

if __name__ == "__main__":
    app.run(debug=True)