import edit_distance
import sys

if sys.argv[-1] == "--help" or sys.argv[-1] == "-h":
    print(
        """
        Created by Arina Batyrbaeva
        КН-104 / МЕН-190201
        Программа проверяет наличие ошибок
        в тексте на английском языке
        и выводит их на экран,
        а так же предлагает свои варианты замены слов
        """
    )


def reading_dictionary_file(dictionaryFilename):
    dictWords = []
    with open(dictionaryFilename, "r") as inputFile:
        for line in inputFile:
            word = line.strip()
            dictWords.append(word.lower())
    return dictWords


def reading_text_file(textFilename):
    words = []
    with open(textFilename, "r") as inputFile:
        for line in inputFile:
            wordsLines = line.strip().split()
            for word in wordsLines:
                words.append(word.strip(" .,!\":;?").lower())
    return words


def finding_mistakes(dictWords, textWords):
    misspelledWords = []
    for word in textWords:
        if word not in dictWords:
            misspelledWords.append(word)
    return misspelledWords


def printing_mistakes(mistakesList):
    print("The misspelled words are: ")
    print('  ')
    for word in mistakesList:
        print(word)


def finding_correct_words(misspelledWords, dictWords):
    autocorrectionWords = []
    for mistake in misspelledWords:
        mindistance = 10000000000000
        for word in dictWords:
            levenshtein_distance = \
                edit_distance.levenshtein_distance(mistake, word)
            if levenshtein_distance < mindistance:
                mindistance = levenshtein_distance
                correct_word = word
                if mindistance == 1:
                    break
        autocorrectionWords.append(correct_word)
    return autocorrectionWords


def printing_correct_words(autocorrection):
    print("The correct words are: ")
    print('  ')
    for word in autocorrection:
        print(word)


def main():
    print("This is the spellchecker. Welcome!")
    dictonaryFile = input("Please enter the dictionary file: ")
    textFile = input("Please enter the text file: ")
    dictionaryList = reading_dictionary_file(dictonaryFile)
    textList = reading_text_file(textFile)
    mistakesList = finding_mistakes(dictionaryList, textList)
    autocorrectionList = finding_correct_words(mistakesList, dictionaryList)
    print('  ')
    printing_mistakes(mistakesList)
    print('  ')
    printing_correct_words(autocorrectionList)


if __name__ == "__main__":
    main()
