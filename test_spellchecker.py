import spellchecker1
import edit_distance
import unittest


class spellchecker_tests(unittest.TestCase):

    def test_edit_distance(self):
        self.assertEqual(edit_distance.levenshtein_distance(
            'champgne', 'champagne'), 1)
        self.assertEqual(edit_distance.levenshtein_distance(
            'silky', 'silky'), 0)

    def test_reading_dictionary_file(self):
        dictionaryFilename = 'test_dict.txt'
        self.assertEqual(spellchecker1.reading_dictionary_file
                         (dictionaryFilename), [
                            'sipping', 'champagne', 'in',
                            'a', 'silky', 'white', 'dress',
                            'lounging', 'on', 'windowseat',
                            'how', 'was', 'this', 'year',
                            'for', 'me', 'i', 'am', 'glad',
                            'you', 'asked', 'do', 'you',
                            'mind', 'holding', 'this', 'glass',
                            'while', 'throw', 'myself',
                            'out', 'the', 'window'
                                                ])

    def test_reading_text_file(self):
        textFilename = 'test_text.txt'
        self.assertEqual(spellchecker1.reading_text_file(textFilename),
                         ['me', 'sipping', 'champagne', 'in',
                          'a', 'silky', 'white', 'dress',
                          'lounging', 'on', 'a',
                          'windowseat', 'how', 'was',
                          'this', 'year', 'for', 'me',
                          'i', 'am', 'glad', 'you', 'asked', 'do',
                          'you', 'mind', 'holding', 'this', 'glass',
                          'while', 'i', 'throw', 'myself',
                          'out', 'the', 'window'])

    def test_finding_mistakes(self):
        dictionaryList = ['sipping', 'champagne', 'in', 'a',
                          'silky', 'white', 'dress', 'lounging',
                          'on', 'windowseat', 'how', 'was', 'this',
                          'year', 'for', 'me', 'i', 'am', 'glad',
                          'you', 'asked', 'do', 'you', 'mind', 'holding',
                          'this', 'glass', 'while', 'throw',
                          'myself', 'out', 'the', 'window']
        textList = ['me', 'sipping', 'champgne',
                    'in', 'a', 'silky', 'white',
                    'dress', 'lounging', 'on', 'a',
                    'windowseat', 'how', 'was', 'this',
                    'year', 'for', 'me', 'i', 'am', 'glad',
                    'you', 'asked', 'do', 'you', 'mind', 'holding',
                    'this', 'glss', 'while', 'i', 'throw',
                    'myself', 'out', 'the', 'wndow']
        self.assertEqual(spellchecker1.finding_mistakes(dictionaryList,
                                                       textList),
                         ['champgne', 'glss', 'wndow'])

    def test_printing_mistakes(self):
        mistakesList = ['champgne', 'glss', 'wndow']
        self.assertEqual(spellchecker1.printing_mistakes(mistakesList), None)

    def test_finding_correct_words(self):
        misspelledWords = ['champgne', 'glss', 'wndow']
        dictWords = ['sipping', 'champagne', 'in', 'a', 'silky',
                     'white', 'dress', 'lounging', 'on',
                     'windowseat', 'how', 'was', 'this',
                     'year', 'for', 'me', 'i', 'am', 'glad',
                     'you', 'asked', 'do', 'you', 'mind',
                     'holding', 'this', 'glass', 'while',
                     'throw', 'myself', 'out', 'the', 'window']
        self.assertEqual(spellchecker1.finding_correct_words
                         (misspelledWords, dictWords),
                         ['champagne', 'glass', 'window'])

    def test_printing_correct_words(self):
        autocorrection = ['champagne', 'glass', 'window']
        self.assertEqual(spellchecker1.printing_correct_words(autocorrection),
                         None)
