from nltk.corpus import words

class Word:

	# get nouns
    def getNouns(self, posTagged):
        nouns = []
        for word, pos in posTagged:
            if pos == 'NN' or pos == 'NNS' or pos == 'NNP' or pos == 'NNPS':
                nouns.append(word)
        return nouns

    # get verbs
    def getVerbs(self, posTagged):
        verbs = []
        for word, pos in posTagged:
            if pos == 'VB' or pos == 'VBD' or pos == 'VBG' or pos == 'VBN' or pos == 'VBP' or pos == 'VBZ':
                verbs.append(word)
        return verbs

    # get adjectives
    def getAdjectives(self, posTagged):
        adjectives = []
        for word, pos in posTagged:
            if pos == 'JJ' or pos == 'JJR' or pos == 'JJS':
                adjectives.append(word)
        return adjectives

    # get adverbs
    def getAdverbs(self, posTagged):
        adverbs = []
        for word, pos in posTagged:
            if pos == 'RB' or pos == 'RBR' or pos == 'RBS':
                adverbs.append(word)
        return adverbs

    def checkWord(self, word):
        if word in words.words():
            return True