import os
import sys
from flask import Flask, render_template, request
from chatterbot.comparisons import LevenshteinDistance
from chatterbot import ChatBot
from chatterbot.conversation import Statement

import logging

import train
from reset import reset_instance


app = Flask(__name__)

logging.basicConfig(level=logging.INFO)

ciara_bot = ChatBot("ciara bot", storage_adapter="chatterbot.storage.SQLStorageAdapter", preprocessors=['chatterbot.preprocessors.clean_whitespace'],
                    logic_adapters=[{
                        'import_path': 'chatterbot.logic.BestMatch',
                        'default_response': 'Sorry, I dont understand',
                        'threshold': 0.28,
                    }])


@app.route("/")
def home():
    return render_template("index.html")


# noinspection PyRedundantParentheses
@app.route("/get")
def get_bot_response():
    userText = Statement(request.args.get('msg'))

    print(ciara_bot.get_response(userText))
    response = str(ciara_bot.get_response(userText))
    return response


if __name__ == '__main__':
    if len(sys.argv) > 2 and sys.argv[1] == '--train':
        dataset = sys.argv[2]

        reset_instance(ciara_bot)
        if not  os.path.isfile(dataset):
            raise ValueError(f'{dataset} is not a valid file. Check its path.')

        train.trainbotbylist(ciara_bot, dataset)

    app.run(debug=True)
