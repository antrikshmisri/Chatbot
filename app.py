from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.response_selection import get_first_response
from chatterbot.comparisons import levenshtein_distance

app = Flask(__name__)

english_bot = ChatBot("Ciara Bot", storage_adapter="chatterbot.storage.SQLStorageAdapter", preprocessors=['chatterbot.preprocessors.clean_whitespace'],logic_adapters=["chatterbot.logic.BestMatch", "chatterbot.logic.MathematicalEvaluation"],trainer='chatterbot.trainers.ListTrainer',read_only=True)
trainer = ChatterBotCorpusTrainer(english_bot)
trainer.train("chatterbot.corpus.english")
trainer.train("C:/Users/antri/PycharmProjects/flask-chatbot/dataset.json")

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    if(userText == "what is your name" or userText == "who are you" or userText == "what is your name?"):
        return str("My name is Ciara Bot")
    elif(userText == "i am antriksh"):
        return str("Hi! Antriksh")
    else:
        return str(english_bot.get_response(userText))


if __name__ == '__main__':
    app.run()