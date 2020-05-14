import edit_distance
from math import ceil
import multiprocessing

def finding_mistakes(dictWords, textWords):
    misspelledWords =[]
    misspelledWords1 = []
    misspelledWords2 = []
    misspelledWords3 = []
    misspelledWords4 = []
    part_len = ceil(len(textWords) / 4)
    lists_of_words = [textWords[part_len * k:part_len * (k + 1)]
                      for k in range(4)]

    p1 = multiprocessing.Process(target=see, args = (lists_of_words[0], dictWords, misspelledWords1))
    p2 = multiprocessing.Process(target=see, args = (lists_of_words[1], dictWords, misspelledWords2))
    p3 = multiprocessing.Process(target=see, args = (lists_of_words[2], dictWords, misspelledWords3))
    p4 = multiprocessing.Process(target=see, args = (lists_of_words[3], dictWords, misspelledWords4))
    p1.start()
    p2.start()
    p3.start()
    p4.start()
    p1.join()
    p2.join()
    p3.join()
    p4.join()

    misspelledWords = p1.Value() + p2.Value() + p3.Value() + p4.Value()
    return misspelledWords


def see(list_of_words, dictWords, misspelledWords):
    for word in list_of_words:
        if word not in dictWords:
            misspelledWords.append(word)
    return misspelledWords

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