import json
import input
from chatterbot.trainers import ListTrainer

def ToString(s):
    # initialize an empty string
    str1 = " "
    # return string
    return (str1.join(s))

with open('intents.json','r') as f:
    intents = json.load(f)



statements = []
ignore_words = ['.', ',', '?', '!']
def inputdata():
    answerindex = 0
    for intent in intents['intents']:
        for pattern in intent['patterns']:
            if(answerindex >= len(intent['responses'])-1):
                answerindex=0
            else:
                answerindex+=1
            q = input.tokenize(pattern.lower())
            a = input.tokenize(intent['responses'][answerindex].lower())
            for word in q:
                if word in ignore_words:
                    q.remove(word)
            for word in a:
                if word in ignore_words:
                    a.remove(word)
            statements.append(ToString(q))
            statements.append(ToString(a))
    return statements

#hyperparameters
iter = 10
def trainbot(chatbot,iter):
    if(iter == 0):
        return "Sucessfully Trained Chatbot"
    iter -= 1
    trainer = ListTrainer(chatbot)
    trainer.train(inputdata())
    print("training the chatbot , iteration No:-" + str(iter))
    trainbot(chatbot , iter)





