import nltk
import re
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag
import requests
from bs4 import BeautifulSoup


# def preprocess(sent):
#    sent = nltk.word_tokenize(sent)
#    sent = nltk.pos_tag(sent)
#    return sent

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
                        try:
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

def news():
    # the target we want to open
    # url = input("Copy the LinkedIn Job description page here: ")
    url = 'http://www.hindustantimes.com/top-news'
    classname = "jobs-box__html-content jobs-description-content__text t-14 t-black--light t-normal"

    # open with GET method
    resp = requests.get(url)

    # http_respone 200 means OK status
    if resp.status_code == 200:
        print("Successfully opened the web page")
        print("The job descriptions are as follow :-\n")

        # we need a parser,Python built-in HTML parser is enough .
        soup = BeautifulSoup(resp.text, 'html.parser')

        # l is the list which contains all the text i.e news
        jd = soup.find("ul", {"class": classname})

        # now we want to print only the text part of the anchor.
        # find all the elements of a, i.e anchor
        for i in l.findAll("a"):
            print(i.text)
    else:
        print("Error")


news()


if __name__ == '__main__':
    hi = heatmapLevelGenerator()
    hi.reader('test.txt')


