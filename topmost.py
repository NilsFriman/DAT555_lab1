from wordfreq import tokenize, countWords, printTopMost
from sys import argv
from urllib import request

def main(arguments):
    
    # with open() does the same as opening and then using close()
    with open(arguments[1], encoding="UTF-8") as file:
        stopwords = []
        for word in file.readlines():
            stopwords.append(word.strip())
    
    if arguments[2].find("http://") == 0 or arguments[2].find("https://") == 0:  # URL link supplied
        response = request.urlopen(arguments[2])
        document = response.read().decode("UTF-8").splitlines()
    else:   
        # with open() does the same as opening and then using close()
        with open(arguments[2], encoding="UTF-8") as file:
            document = file.readlines()

    # We will print the top n most frequent tokens
    n = int(arguments[3])

    tokens = tokenize(document)
    frequencies = countWords(tokens, stopwords)
    printTopMost(frequencies, n)

main(argv)
