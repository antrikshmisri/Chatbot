import app
import reset


def read_file():
    with open("intents.json", "r") as f:
        before = f.readlines()
    return before

def ischanged():
    initial = read_file()
    while True:
        current = read_file()
        if(initial != current):
            print('Change Detected , Rebuilding Bot')
            reset.resetInstance(app.ciara_bot)
            initial = current

ischanged()