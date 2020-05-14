import reading_texts
import printing_words
import finding_words
import argparse
import sys
import time
import multiprocessing
from multiprocessing import Process



def main():

    parser = argparse.ArgumentParser(
        description='enter the dicitionary/text file')
    parser.add_argument('dictionary', type=str, metavar='', default='console',
                        help='enter the name of dictionary file')
    parser.add_argument('text', type=str, metavar='', default='console',
                        help='enter the name of text file')
    args = parser.parse_args()

    dictionaryFile = args.dictionary
    textFile = args.text

    start = time.perf_counter()

    print("This is the spellchecker. Welcome!")

    dictionaryList = reading_texts.reading_dictionary_file(dictionaryFile)
    textList = reading_texts.reading_text_file(textFile)
    mistakesList = finding_words.finding_mistakes(dictionaryList, textList)
    autocorrectionList = \
        finding_words.finding_correct_words(mistakesList, dictionaryList)
    print('  ')
    printing_words.printing_mistakes(mistakesList)
    print('  ')
    printing_words.printing_correct_words(autocorrectionList)

    finish = time.perf_counter()
    print(f'finished in {round(finish - start, 2)} second(s)')


if __name__ == "__main__":
    main()