import edit_distance

def finding_mistakes(dictWords, textWords):
    misspelledWords = []
    for word in textWords:
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