from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__, template_folder=".")

responses = [
    "Yes, definitely",
    "No way",
    "Ask again later",
    "It is certain",
    "Very doubtful",
    "Signs point to yes",
    "Better not tell you now",
    "Absolutely",
    "I don't think so",
    "Without a doubt",
]

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask():
    user_question = request.json.get("question")
    answer = random.choice(responses)
    return jsonify({"answer": answer})

if __name__ == "__main__":
    app.run(debug=True)
