def tokenize(document):

    tokens = []  # Empty list of tokens, which we will fill.

    for line in document:

        start = 0  # Starting index of token substring
        end = 0  # Ending index of token substring (non-inclusive)

        token_type = None  # The type of token we are currently working with. None means we aren't currently building a token

        for character in line:

            # We find out the type of character we are working with
            if character.isalpha(): character_type = "letter"
            elif character.isdigit(): character_type = "digit"
            else: character_type = None

            if character_type:  # We are working with a digit or letter

                if token_type and token_type != character_type:  # Token in progress, but the type doesn't match
                    tokens.append(line[start: end])  # Finish the token

                end += 1  # Increment the index, regardless of if we start a new token or not

                if token_type != character_type:  # The types don't match -> we start a new token
                    start = end - 1
                    token_type = character_type

            else:  # We are working with a space or special character
                
                if token_type:  # Token in progress
                    tokens.append(line[start: end].lower())  # Finish the token
                    token_type = None  # Reset the token type
                
                if not character.isspace():  # We are working with a special character
                    tokens.append(line[end])  # Add the character

                # Increment indices
                end += 1
                start = end

        if token_type:  # Token in progress when we are finished with the whole line
            tokens.append(line[start: end].lower())  # Add the token

    return tokens


#Counting
def countWords(words, stopWords):

    counter = {}

    for element in words: 
        if element not in stopWords:
            if element not in counter:
                counter[element] = 0
            counter[element] += 1

    return counter  

#Printing
def printTopMost(frequencies,n):
    sorted_freq = sorted(frequencies.items(), key=lambda x: -x[1])
    if sorted_freq != []:
        for i in range(n):
            word = sorted_freq[i][0]
            occurence = str(sorted_freq[i][1])
            table_freq = word.ljust(20) + occurence.rjust(5)
            print(table_freq)

