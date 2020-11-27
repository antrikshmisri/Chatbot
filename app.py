from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.conversation import Statement

import chatterbot
import logging


import train





app = Flask(__name__)


logging.basicConfig(level=logging.INFO)
ciara_bot = ChatBot("ciara bot", storage_adapter="chatterbot.storage.SQLStorageAdapter", preprocessors=['chatterbot.preprocessors.clean_whitespace'],
            logic_adapters=[{
            'import_path': 'chatterbot.logic.BestMatch',
            'default_response': 'Sorry, I dont understand',
            'maximum_similarity_threshold': 0.8
             },
             "chatterbot.logic.MathematicalEvaluation"])

train.trainbotbylist(ciara_bot,10)
train.trainbotbyubuntu(ciara_bot,1)



@app.route("/")
def home():
    return render_template("index.html")


# noinspection PyRedundantParentheses
@app.route("/get")
def get_bot_response():
    userText = Statement(request.args.get('msg'))
    if(userText == "i am antriksh"):
        return str("Hi! Antriksh")
    elif(userText == 'who made you' or userText == 'who is your father'):
        return str('A guy named Antriksh made me')
    else:
        print(ciara_bot.get_response(userText))
        response = str(ciara_bot.get_response(userText))
        return response


if __name__ == '__main__':
    app.run()