import nltk
from nltk.stem.porter import PorterStemmer
nltk.download('punkt')

def tokenize(sentence):
    return nltk.tokenize(sentence)


stemmer = PorterStemmer()
def stem(words):
    return stemmer.stem(words.lower())


