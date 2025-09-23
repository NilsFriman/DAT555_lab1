def tokenize(document):

    words = []  # lowercase, separated using only spaces.

    for line in document:
        for word in line.lower().split():
            words.append(word)

    # We still need to handle words with letters AND numbers, as well as special characters.

    # A help function to find the type of character
    def char_type(checking_character):

        letters = "abcdefghijklmnopqrstuvwxyz"
        numbers = "0123456789"

        if checking_character in letters:
            return "letter"
        if checking_character in numbers:
            return "number"
        return "special"

    tokens = []

    for word in words:

        token = ""
        token_type = None

        for character in word:

            character_type = char_type(character)
            
            if character_type == token_type:
                token += character
                continue
            
            if token:
                tokens.append(token)
                token = character
                token_type = character_type

                if token_type == "special":
                    tokens.append(token)
                    token = ""
                    token_type = None
            
            else:  # New token
                token = character
                token_type = character_type
        
        if token:  # Appends the token in progress, if there is one
            tokens.append(token)
    
    return tokens
