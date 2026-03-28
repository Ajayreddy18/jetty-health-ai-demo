from flask import Flask, request, jsonify
from flask_cors import CORS
import ollama

app = Flask(__name__)
CORS(app)

@app.route("/ask", methods=["POST"])
def ask():
    data = request.json
    question = data.get("question", "")

    # Better system prompt (important)
    messages = [
        {
            "role": "system",
            "content": "You are a helpful AI health assistant. Give short, clear, supportive answers. Do not give dangerous medical advice."
        },
        {
            "role": "user",
            "content": question
        }
    ]

    response = ollama.chat(
        model="tinyllama",
        messages=messages
    )

    answer = response["message"]["content"]

    return jsonify({"answer": answer})


if __name__ == "__main__":
    app.run(port=5000, debug=True)