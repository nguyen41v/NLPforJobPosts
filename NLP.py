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


