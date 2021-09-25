import json
from itertools import count
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import UbuntuCorpusTrainer


def ToString(s):
    # initialize an empty string
    str1 = " "
    # return string
    return (str1.join(s))


def inputdata(file='intents.json'):
    """Process the input data to a list of statements.

    Parameters
    ----------
    file : str
        The path to the input file.

    Returns
    -------
    list
        A list of statements representing a conversation.
    """
    with open(file, 'r') as f:
        dataset = json.load(f)

    if file == 'english-train.json':
        statements = []
        for conversation in dataset:
            question = conversation['utterances'][0].lower().split('patient:')[1]
            fullstop_questions = question.split('.')

            answer = conversation['utterances'][1].lower().split('doctor:')[1]

            for f_question in fullstop_questions:
                statements.append([f_question, answer])

            statements.append([question, answer])

        return statements
    
    elif file == 'train_light.json':
        statements = []
        for obj in dataset:
            annotation_dict = obj['annotations'][0]
            question_type = annotation_dict['type']
            if question_type == 'multipleQAs':
                question_objs = annotation_dict['qaPairs']
                for obj in question_objs:
                    question = obj['question'].lower()
                    answer = obj['answer'][0].lower()
                    statements.append([question, answer])
            elif question_type == 'singleAnswer':
                question = obj['question'].lower()
                annotation_dict = obj['annotations'][0]
                answer = annotation_dict['answer'][0].lower()
                statements.append([question, answer])
    
    elif file == 'intents.json':
        statements = []
        obj = dataset['intents']
        
        for intent in obj:
            questions = intent['patterns']
            answer = intent['responses']

            for question, answer in zip(questions, answer):
                statements.append([question.lower(), answer.lower()])

        return statements

# hyperparameters
iter = 10


def trainbotbylist(chatbot, dataset='english-train.json'):
    """Train the chatbot using ListTrainer on a specific dataset.
    
    Parameters
    ----------
    chatbot : ChatBot
        A chatbot instance.
    dataset : str
        The path to the input file.
    """
    trainer = ListTrainer(chatbot)
    data = inputdata(dataset)
    iterator = (count(start=1, step=1))

    for conversation in data:
        trainer.train(conversation)
        statement_count = next(iterator)
    
    print(f'Successfully trained bot with {statement_count} conversations')


def trainbotbyubuntu(chatbot, iter):
    if(iter == 0):
        return "Sucessfully Trained Chatbot"
    iter -= 1
    trainer = UbuntuCorpusTrainer(chatbot)
    trainer.train()
    print("training the chatbot , iteration No:-" + str(iter))
    trainbotbyubuntu(chatbot, iter)
