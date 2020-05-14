import spellchecker1

def reading_dictionary_file(dictionaryFilename):
    dictWords = []
    with open(dictionaryFilename, "r", encoding='utf-8') as inputFile:
        for line in inputFile:
            word = line.strip()
            dictWords.append(word.lower())
    return dictWords


def reading_text_file(textFilename):
    words = []
    with open(textFilename, "r", encoding='utf-8') as inputFile:
        for line in inputFile:
            wordsLines = line.strip().split()
            for word in wordsLines:
                words.append(word.strip(" .,!\":;?").lower())
    return words