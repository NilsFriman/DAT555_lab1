from wordfreq import tokenize, countWords, printTopMost
from sys import argv

def main(arguments):

    with open(arguments[1], encoding="UTF-8") as file:
        stopwords = []
        for word in file.readlines():
            stopwords.append(word.strip())
    
    with open(arguments[2], encoding="UTF-8") as file:
        document = []
        for line in file.readlines():
            document.append(line.strip())

    tokens = tokenize(document)
    frequencies = countWords(tokens, stopwords)
    printTopMost(frequencies, int(arguments[3]))

main(argv)
