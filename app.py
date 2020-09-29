from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer


app = Flask(__name__)

english_bot = ChatBot("Ciara Bot", storage_adapter="chatterbot.storage.SQLStorageAdapter", preprocessors=['chatterbot.preprocessors.clean_whitespace'],
            logic_adapters=[{
            'import_path': 'chatterbot.logic.BestMatch',
            'default_response': 'i honestly have no idea how to respond to that',
            'maximum_similarity_threshold': 0.8
             },
             "chatterbot.logic.MathematicalEvaluation"],
             trainer='chatterbot.corpus.english')
trainer = ChatterBotCorpusTrainer(english_bot)
trainer.train("chatterbot.corpus.english")
print("training with intents.json\n")
trainer.train("./intents.json")
##trainer.export_for_training('./my_export.json')

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