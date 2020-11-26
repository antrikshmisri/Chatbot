from chatterbot import ChatBot
import app,train
def resetInstance(chatbot):
    print('resetting instance of :-' + str(chatbot))
    bot = ChatBot(chatbot)
    bot.storage.drop()
    print('Successfully Dropped The Data')
    print('Training With Changed Dataset')
    train.trainbot(app.ciara_bot, 10)

