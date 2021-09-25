"""Module to provide utilityb functions for resetting chatbots"""

def reset_instance(chatbot):
    print('resetting instance of :-' + str(chatbot))
    chatbot.storage.drop()
    print('Successfully Dropped The Data')

if __name__ == "__main__":
    from app import ciara_bot
    reset_instance(ciara_bot)