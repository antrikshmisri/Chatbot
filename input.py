import nltk
from nltk.stem.porter import PorterStemmer

def downloadData():
    nltk.download('punkt')
    nltk.download('corpora')

def tokenize(sentence):
    return nltk.word_tokenize(sentence)


stemmer = PorterStemmer()
def stem(words):
    return stemmer.stem(words.lower())


