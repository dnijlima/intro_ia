import nltk
from nltk.stem import RSLPStemmer

def Tokenize(sentence):
    sentence = sentence.lower()
    sentence = nltk.word_tokenize(sentence)
    return sentence

def Stemming(sentence):
    stemmer = RSLPStemmer()
    phrase = []
    for word in sentence: 
        phrase.append(stemmer.stem(word.lower()))
    return phrase

stopwords = nltk.corpus.stopwords.words("portuguese")
print (stopwords)
        