from nltk.tokenize import word_tokenize
from spellchecker import SpellChecker


def textPreprocessing(rawText):
    rawText = rawText.lower()  # to lowercase

    rawText = rawText.translate(str.maketrans('', '', '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'))  # remove punctuation

    word_tokenize(rawText)  # tokenize

    rawText = [word for word in word_tokenize(rawText) if
                not any(char.isdigit() for char in word)]  # remove tokens with numbers

    spell = SpellChecker()  # correct misspelled words
    rawText = [spell.correction(word) for word in rawText]

    return rawText