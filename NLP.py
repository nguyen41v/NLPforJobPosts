import nltk
import re
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag

def preprocess(sent):
    sent = nltk.word_tokenize(sent)
    sent = nltk.pos_tag(sent)
    return sent





if __name__ == '__main__':
    ex = 'Proficient in at least one (preferably two) of the following languages: Python, Java, C, C++, C#, Ruby, JavaScript, or another object-oriented language '



