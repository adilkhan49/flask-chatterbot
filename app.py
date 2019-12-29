from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

app = Flask(__name__)

english_bot = ChatBot("Chatterbot", storage_adapter="chatterbot.storage.SQLStorageAdapter")
trainer = ChatterBotCorpusTrainer(english_bot)
trainer.train("chatterbot.corpus.english")

@app.route("/")
def home():
    return "Welcome to chatterbot!"

@app.route("/<msg>")
def get_bot_response(msg):
#    userText = request.args.get('msg')
 	userText = msg
 	return str(english_bot.get_response(userText))


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
