import requests
from bs4 import BeautifulSoup
import operator


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
                line = line.replace('/', ' ').replace(',', ' ')
                words = line.strip().split(' ')  # not accounting for languages that have spaces in them for now
                temps = []  # store words found in this line
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
        print("\nRequired programming languages are as follow:")
        for key, value in sorted(dict_of_language_scores.items(), key=operator.itemgetter(1), reverse=True):
            heatmap_value = 1
            if value >= 2:
                heatmap_value = 2
            if value <= 0:
                heatmap_value = 0
            print(key, heatmap_value)
        print("=" * 44)


    def readerInteractive(self):
        dict_of_language_scores = {}
        filename = input("Which file is the job description in?\n")
        filename = filename.strip()
        while True:
            try:
                with open(filename, 'r') as txtfile:
                    break
            except FileNotFoundError:
                filename = input("Sorry the file was not found. Please try entering in the filename again.\n"
                                 "It might be from a typo or a missing extension.\n")
                filename = filename.strip()
        with open(filename, 'r') as txtfile:
            reader = txtfile.readlines()
            for line in reader:
                line = line.replace('/', ' ').replace(',', ' ')
                words = line.strip().split(' ') # not accounting for languages that have spaces in them for now
                print(words)
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
        print("\nRequired programming languages are as follow:")
        for key, value in sorted(dict_of_language_scores.items(), key=operator.itemgetter(1), reverse=True):
            heatmap_value = 1
            if value >= 2:
                heatmap_value = 2
            if value <= 0:
                heatmap_value = 0
            print(key, heatmap_value)
        print("=" * 44)

    def readerWeb(self, text):
        if not text:
            return
        dict_of_language_scores = {}
        reader = text.split('.')
        preferred = False
        for line in reader:
            line = line.replace('/', ' ').replace(',', ' ')
            words = line.strip().split(' ')  # not accounting for languages that have spaces in them for now
            temps = [] # store words found in this line
            if 'prefer' in line.lower():
                preferred = True
            for word in words:
                word = word.replace(',', '')
                if word in self.languages:
                    if word not in temps and not preferred:
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
        print("\nRequired programming languages are as follow:")
        for key, value in sorted(dict_of_language_scores.items(), key=operator.itemgetter(1), reverse=True):
            heatmap_value = 1
            if value >= 2:
                heatmap_value = 2
            if value <= 0:
                heatmap_value = 0
            print(key, heatmap_value)
        print("=" * 44 + '\n')

    def printJD(self):
        # the target we want to open
        url = input("Paste the Monster Job description page here.\n")
        url = url.strip()
        classname = "jobs-box__html-content jobs-description-content__text t-14 t-black--light t-normal"
        while True:
            # open with GET method
            try:
                resp = requests.get(url)
                break
            except requests.exceptions.MissingSchema:
                url = input("Sorry, that link was not valid. Perhaps you meant http://" + url +'\nPlease reenter the url.')

        # http_respone 200 means OK status
        if resp.status_code == 200:
            print(" - Successfully opened the web page - ")

            # we need a parser,Python built-in HTML parser is enough .
            soup = BeautifulSoup(resp.text, 'html.parser')

            # l is the list which contains all the text i.e news
            # jd = soup.find("ul", id="mylist")
            # jd = soup.find("ul",{"class":classname}).text
            # jd = soup.find("span", {"class": classname, "data-value": True})['data-value']
            jd = str(soup.find(id='JobDescription'))
            # print(jd)
            # print(self.clearTags(jd))
            return self.clearTags(jd)
            # print(jd)
        else:
            print("The webpage was not successfully opened, there may be an error in the address or a login is required to access content.")
            return ""

    def clearTags(self, text):
        # can make it better by chaning the filler, ex '\n', based off of what is in the brackets
        # ex. put spaces between things that are bolded and newlines between headings vs paragraphs
        while text.rfind("<") != -1:
            text = text[:text.rfind("<")] + "\n" + text[text.rfind(">") + 1:]
        return text.strip().replace("     ", " ")

    def main(self):
        direction = input("Hello. This program can parse out programming languages from a job description in a text file or from a job post on Monster.\n"
                          "It will generate levels to them, where 2 means you need to know the language very well,\n"
                          "                                       1 means you should have some knowledge of the language,\n"
                          "                                       0 means you don't need to know the language, but if you do, it's a bonus for the company.\n\n"
                          "What would you like to do?\n"
                          "Enter in \"Text\" to parse from a textfile, \"Monster\" to parse from Monster, or \"Quit\" to quit.\n")
        direction = direction.lower()
        while direction != "quit" and direction != 'no' and direction != 'exit':
            if "text" in direction:
                self.readerInteractive()
                direction = input(
                    "Is there anything else you would like to do?\n"
                    "For reference, enter in \"Text\" to parse from a textfile, \"Monster\" to parse from Monster, or \"Quit\" to quit.\n")
                direction = direction.lower()
            elif "monster" in direction:
                self.readerWeb(self.printJD())
                direction = input(
                    "Is there anything else you would like to do?\n"
                    "For reference, enter in \"Text\" to parse from a textfile, \"Monster\" to parse from Monster, or \"Quit\" to quit.\n")
                direction = direction.lower()
            else:
                direction = input("Sorry that was not a valid input. Please enter in your choice again.\n"
                                  "For reference, enter in \"Text\" to parse from a textfile, \"Monster\" to parse from Monster, or \"Quit\" to quit.\n")
        print("Good luck job hunting.")


if __name__ == '__main__':
    hi = heatmapLevelGenerator()
    # hi.reader('test.txt')
    hi.main()
    # hi.readerWeb(hi.printJD())
    # hi.readerInteractive()
