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
    for intent in intents['intents']:
        for pattern,response in zip(intent['patterns'] , intent['responses']):
            q = input.tokenize(pattern)
            a = input.tokenize(response)
            for idx,word in enumerate(q):
                q[idx] = input.stem(word)
                if word in ignore_words:
                    q.remove(word)
            for idx,word in enumerate(a):
                a[idx] = input.stem(word)
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





