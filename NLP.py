import nltk
import re
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag

def preprocess(sent):
    sent = nltk.word_tokenize(sent)
    sent = nltk.pos_tag(sent)
    return sent

class heatmapLevelGenerator():
    def __init__(self):
        self.languages = []
        with open('txtFileofLanguages.txt', 'r') as txtfile:
            reader = txtfile.readlines()
            for line in reader:
                self.languages.append(line.strip())

        self.valueOne = []
        with open('valueOne.txt', 'r') as txtfile:
            reader = txtfile.readlines()
            for line in reader:
                print(line.strip())
                self.valueOne.append(line.strip())

        self.valueTwo = []
        with open('valueOne.txt', 'r') as txtfile:
            reader = txtfile.readlines()
            for line in reader:
                self.valueTwo.append(line.strip())

        self.valueNegative = []
        with open('valueOne.txt', 'r') as txtfile:
            reader = txtfile.readlines()
            for line in reader:
                self.valueNegative.append(line.strip())


    def reader(self, filename):
        dictOfLanguageScores = {}
        with open(filename, 'r') as txtfile:
            reader = txtfile.readlines()
            for line in reader:
                words = line.split(' ') # not accounting for languages that have spaces in them for now
                for word in words:
                    if word in self.languages:
                        try:
                            dictOfLanguageScores[word]
                        except KeyError:
                            dictOfLanguageScores[word] = 0





if __name__ == '__main__':
    hi = heatmapLevelGenerator()
    hi.reader('test.txt')


