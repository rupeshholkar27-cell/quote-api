from flask import Flask, jsonify
import random

app = Flask(__name__)

QUOTES = [
    "Believe you can and you're halfway there.",
    "Practice makes progress.",
    "Small steps every day lead to big results.",
    "Mistakes are proof that you are trying.",
    "Every expert was once a beginner.",
]

@app.route("/quote")
def quote():
    return jsonify({"quote": random.choice(QUOTES)})

@app.route("/health")
def health():
    return jsonify({"status": "ok"})

@app.route("/hello")
def hello():
    return jsonify({"message": "Hello from the Quote API!"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)