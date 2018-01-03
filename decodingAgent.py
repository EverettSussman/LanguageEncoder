"""
Agent that solves decoding problems
using a bayesian framework.
"""
from utils import *
import csv
import numpy as np

MAXINT = 10000000
#*********************************#

class simplePairAgent():
    """
    This agent determines which key is most
    likely to result in an english decoding
    by minimizing
    -log_10(P(x_1 | x_0) * P(x_2 | x_1) ...),
    where the transition probabilities are
    found from an analysis of the english
    language.
    """

    def __init__(self):

        self.transProbs = {}
        # Fill in dictionary with transition probabilities
        with open('pairFrequency.csv', 'r') as pairFile:
            data = csv.reader(pairFile)
            for row in data:
                letter0 = row[0].split("'")[1]
                letter1 = row[1].split("'")[1]

                # Denote end of word with None
                if letter1 == '\\n':
                    letter1 = None

                val = float(row[2])
                self.transProbs[(letter0, letter1)] = val

        self.log = {}

    def decode(self, message):

        bestKey = None
        bestScore = MAXINT
        for key in range(26):
            newMessage = encode(message, key=key)
            newScore = self.score(newMessage)
            if newScore < bestScore:
                bestScore, bestKey = newScore, key
            print(" key: {}\n newMessage: {}\n \
                    newScore: {}".format(key,
                                    newMessage, newScore))
        print(" Best key: {}\n \
                Best Decoding: {}".format(bestKey,
                    encode(message, key=bestKey)))
        return (bestKey)

    def score(self, string):
        runProd = 1
        for i in range(len(string) - 1):
            if string[i].isalpha():
                letter0 = string[i].lower()
                # Check if end of word
                if not string[i+1].isalpha():
                    runProd *= self.transProbs[(letter0, None)]
                else:
                    letter1 = string[i+1].lower()
                    runProd *= self.transProbs[(letter0, letter1)]
            else:
                continue
        return -1 * np.log10(runProd)



keyGenerator = gensym()
test = simplePairAgent()

testMessage = encode("Hi da!  Do you wan to chek out the USSR yonight?")
print(testMessage)
key = test.decode(testMessage)
print(key)
