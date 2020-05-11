import reading_texts
import printing_words
import finding_words

def main():
    print("This is the spellchecker. Welcome!")
    dictonaryFile = input("Please enter the dictionary file: ")
    textFile = input("Please enter the text file: ")
    dictionaryList = reading_texts.reading_dictionary_file(dictonaryFile)
    textList = reading_texts.reading_text_file(textFile)
    mistakesList = finding_words.finding_mistakes(dictionaryList, textList)
    autocorrectionList = \
        finding_words.finding_correct_words(mistakesList, dictionaryList)
    print('  ')
    printing_words.printing_mistakes(mistakesList)
    print('  ')
    printing_words.printing_correct_words(autocorrectionList)


if __name__ == "__main__":
    main()
