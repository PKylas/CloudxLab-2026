from flask import Flask, render_template, request, jsonify, session
from openai import OpenAI
from dotenv import load_dotenv
import os
import uuid

load_dotenv()

app = Flask(__name__)

app.secret_key = os.getenv("FLASK_SECRET_KEY", "dev-secret-key-change-this")

if not os.getenv("OPENAI_API_KEY"):
    raise RuntimeError("OPENAI_API_KEY is missing. Add it to your .env file.")

client = OpenAI()

system_prompt = """
You answer the user's questions in the spirit of a sarcastic customer service executive.
"""

MODEL = os.getenv("OPENAI_MODEL", "gpt-5.4-nano")

conversations = {}


class Chatbot:
    def __init__(self):
        self.messages = [
            {
                "role": "system",
                "content": system_prompt,
            }
        ]
        self.total_input_tokens = 0
        self.total_output_tokens = 0
        self.total_tokens = 0

    def ask_bot(self, question):
        self.messages.append({"role": "user", "content": question})

        response = client.chat.completions.create(
            model=MODEL,
            messages=self.messages
        )

        answer = response.choices[0].message.content

        self.messages.append({"role": "assistant", "content": answer})

        if response.usage:
            self.total_input_tokens += response.usage.prompt_tokens
            self.total_output_tokens += response.usage.completion_tokens
            self.total_tokens += response.usage.total_tokens

        return answer

    def usage(self):
        return {
            "input_tokens": self.total_input_tokens,
            "output_tokens": self.total_output_tokens,
            "total_tokens": self.total_tokens,
        }


def get_chatbot():
    if "chat_id" not in session:
        session["chat_id"] = str(uuid.uuid4())

    chat_id = session["chat_id"]

    if chat_id not in conversations:
        conversations[chat_id] = Chatbot()

    return conversations[chat_id]


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_message = data.get("message", "").strip()

    if not user_message:
        return jsonify({
            "error": "Message cannot be empty."
        }), 400

    if user_message.lower() in ["exit", "quit", "bye"]:
        bot = get_chatbot()
        return jsonify({
            "answer": "May the fourth be with you.",
            "usage": bot.usage(),
            "done": True
        })

    bot = get_chatbot()

    try:
        answer = bot.ask_bot(user_message)

        return jsonify({
            "answer": answer,
            "usage": bot.usage(),
            "done": False
        })

    except Exception as e:
        return jsonify({
            "error": str(e)
        }), 500


app.route("/reset", methods=["POST"])
def reset():
    chat_id = session.get("chat_id")

    if chat_id and chat_id in conversations:
        del conversations[chat_id]

    session.pop("chat_id", None)

    return jsonify({
        "status": "reset"
    })


if __name__ == "__main__":
    app.run(debug=True)