from chatterbot import ChatBot

def resetInstance(chatbot):
    print('resetting instance of :-' + str(chatbot))
    bot = ChatBot(chatbot)
    bot.storage.drop()

