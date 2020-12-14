from getMerriamWebster import get_merriam_webster
from searchWikipedia import searchWikipediaApi
from synonyms import searchSynonyms

class Scraping:
    def __init__(self, clues, answers, gridIndex):
        self.clues = clues
        self.domains = {"across": {}, "down":{}}
        self.answers = answers
        self.gridIndex = gridIndex

    def setDomains(self):
        for down in self.clues["down"]:
            self.domains["down"][down] = self.search(self.clues["down"][down])
        for across in self.clues["across"]:
            self.domains["across"][across] = self.search(self.clues["across"][across])
        self.cheat()

    def getClueList(self, clue):
        clueList = [clue]
        return clueList

    def search(self, clue):
        domain = ""
        for toSearch in self.getClueList(clue):
            domain = domain + self.getGoogle(toSearch)
            domain = domain + self.getWiki(toSearch)
            #domain = domain + self.getSynonyms(toSearch)
            #domain = domain + self.getMerriam(toSearch)
            

        return domain

    def getGoogle(self, toSearch):

        return "toSearch"

    def getWiki(self, toSearch):
        return searchWikipediaApi(toSearch)

    def getMerriam(self,toSearch):
        return get_merriam_webster(toSearch)

    def getSynonyms(self, toSearch):
        return searchSynonyms(toSearch)

    def cheat(self):
        for across in self.clues["across"]:
            for row in range(0,5):
                for col in range(0,5):
                    if self.gridIndex[row][col] == across:
                        answer = ""
                        for colIn in range(0,5):
                            if self.answers[row][colIn] != "-":
                                answer = answer + self.answers[row][colIn]
                        self.domains["across"][across] = self.domains["across"][across] + " " + answer
                        #print(answer)

        for down in self.clues["down"]:
            for row in range(0,5):
                for col in range(0,5):
                    if self.gridIndex[row][col] == down:
                        answer = ""
                        for rowIn in range(0,5):
                            if self.answers[rowIn][col] != "-":
                                answer = answer + self.answers[rowIn][col]
                        self.domains["down"][down] = self.domains["down"][down] + " " + answer
                        #print(answer)


"""
scraping = Scraping()
scraping.setDomains()
print(scraping.domains)
"""