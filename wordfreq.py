# TODO: The function lacks exception handling. It assumes that document is a list of strings.
def tokenize(document):

    words = []  # Creates an empty list of words

    for line in document:
        for word in line.lower().split():  # Separates each string into "words" defined by spaces, and makes sure everything is lowercase
            words.append(word)  # Fills the list of words

    # We still need to handle words with:
    # 1. letters AND numbers
    # 2. special characters

    # A help function to find the type of a character
    def char_type(checking_character):

        letters = "abcdefghijklmnopqrstuvwxyz"
        numbers = "0123456789"

        if checking_character in letters:
            return "letter"
        elif checking_character in numbers:
            return "number"
        else:
            return "special"

    tokens = []  # Creates an empty list of tokens

    for word in words:  # Loops over every lowercase, space separated word

        # Creates empty variables which define the "token in progress"
        token = ""
        token_type = None

        for character in word:  # Loops over every character in each word

            character_type = char_type(character)

            if character_type == token_type:  # The character matches the token in progress
                token += character

            elif token:  # The character doesn't match an existing token in progress

                tokens.append(token)  # Adds the token to the list of tokens
                token = character  # Starts a new token with the current character
                token_type = character_type  # Updates character type

                if token_type == "special":  
                    
                    # If it is a special character, we need to add it immediately,
                    # since tokens with special characters are only one character long

                    tokens.append(token)
                    token = ""
                    token_type = None

            else:  # New token is being started (a token doesn't exist right now)
                token = character
                token_type = character_type

        if token:  # Appends the token in progress when a word is completed, if there is one
            tokens.append(token)

    # Our list of tokens is done. Returns the list
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

