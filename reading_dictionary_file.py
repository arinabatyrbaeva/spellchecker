def reading_dictionary_file(dictionaryFilename):
    dictWords = []
    with open(dictionaryFilename, "r") as inputFile:
        for line in inputFile:
            word = line.strip()
            dictWords.append(word.lower())
    return dictWords