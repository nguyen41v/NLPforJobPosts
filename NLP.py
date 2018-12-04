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
        with open('valueOne.txt', 'r') as txtfile1:
            reader1 = txtfile1.readlines()
            for line in reader1:
                self.valueOne.append(line.strip())

        self.valueTwo = []
        with open('valueTwo.txt', 'r') as txtfile2:
            reader2 = txtfile2.readlines()
            for line in reader2:
                self.valueTwo.append(line.strip())

        self.valueNegative = []
        with open('valueNegative.txt', 'r') as txtfile3:
            reader3 = txtfile3.readlines()
            for line in reader3:
                self.valueNegative.append(line.strip())


    def reader(self, filename):
        dict_of_language_scores = {}
        with open(filename, 'r') as txtfile:
            reader = txtfile.readlines()
            for line in reader:
                words = line.strip().split(' ') # not accounting for languages that have spaces in them for now
                temps = [] # store words found in this line
                for word in words:
                    if word in self.languages:
                        if word not in temps:
                            temps.append(word)
                        try: # checking to see if word has been added to dict before, if not, add it and initialize it with a value of 0
                            dict_of_language_scores[word]
                        except KeyError:
                            dict_of_language_scores[word] = 0
                # assume that all words apply to all languages that appear in that sentence
                for word in words:
                    if word in self.valueOne:
                        for temp in temps:
                            dict_of_language_scores[temp] += 1
                    if word in self.valueTwo:
                        for temp in temps:
                            dict_of_language_scores[temp] += 2
                    if word in self.valueNegative:
                        for temp in temps:
                            dict_of_language_scores[temp] -= 1
        for key, value in dict_of_language_scores.items():
            heatmap_value = 1
            if value >= 2:
                heatmap_value = 2
            if value <= 0:
                heatmap_value = 0
            print(key, heatmap_value)





if __name__ == '__main__':
    hi = heatmapLevelGenerator()
    hi.reader('test.txt')


