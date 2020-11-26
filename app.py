from flask import Flask, render_template, request
from chatterbot import ChatBot

import chatterbot
import nltk.corpus
import os

import input as nlplib
import train
import reset




app = Flask(__name__)

if(not os.listdir(nltk.data.find("corpora"))):
    print('data not found , downloading resources...')
    nlplib.downloadData()

ciara_bot = ChatBot("ciara bot", storage_adapter="chatterbot.storage.SQLStorageAdapter", preprocessors=['chatterbot.preprocessors.clean_whitespace'],
            logic_adapters=[{
            'import_path': 'chatterbot.logic.BestMatch',
            'default_response': 'i honestly have no idea how to respond to that',
            'maximum_similarity_threshold': 0.5
             },
             "chatterbot.logic.MathematicalEvaluation"])

train.trainbot(ciara_bot,10)



@app.route("/")
def home():
    return render_template("index.html")


# noinspection PyRedundantParentheses
@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg').lower()
    if(userText == "i am antriksh"):
        return str("Hi! Antriksh")
    elif(userText == 'who made you' or userText == 'who made you?' or userText == 'who is your father'):
        return str('A guy named Antriksh made me')
    else:
        print(ciara_bot.get_response(userText))
        return str(ciara_bot.get_response(userText))


if __name__ == '__main__':
    app.run()