from words import Word
from nltk.stem import WordNetLemmatizer

class WordProcessing:

    wordForm = Word()

    def generatePossibleWords(self, word, prefixes, suffixes):
        outputWords = []
        for prefix in prefixes:
            for suffix in suffixes:
                outputWords.append(prefix + word + suffix)
        return outputWords

    def lemmatizeText(self, preprocessedText):
        nouns = self.wordForm.getNouns(preprocessedText)
        verbs = self.wordForm.getVerbs(preprocessedText)
        adjectives = self.wordForm.getAdjectives(preprocessedText)
        adverbs = self.wordForm.getAdverbs(preprocessedText)

        # lemmatize by pos tags
        lemmatizer = WordNetLemmatizer()
        nouns = [lemmatizer.lemmatize(word, pos='n') for word in nouns]
        verbs = [lemmatizer.lemmatize(word, pos='v') for word in verbs]
        adjectives = [lemmatizer.lemmatize(word, pos='a') for word in adjectives]
        adverbs = [lemmatizer.lemmatize(word, pos='r') for word in adverbs]

        return nouns + verbs + adjectives + adverbs  # unite into text
