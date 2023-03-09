class ProcessedWord:
    def __init__(self, lemma, pos, correctPrefixes, correctSuffixes):
        self.lemma = lemma
        self.pos = pos
        self.correctPrefixes = correctPrefixes
        self.correctSuffixes = correctSuffixes

    # __str__ method
    def __str__(self):
        return '{} {} {} {}'.format(self.lemma, self.pos, self.correctPrefixes, self.correctSuffixes)

    # __repr__ method
    def __repr__(self):
        return '{} {} {} {}'.format(self.lemma, self.pos, self.correctPrefixes, self.correctSuffixes)

    # properties
    @property
    def lemma(self):
        return self.__lemma

    @lemma.setter
    def lemma(self, value):
        self.__lemma = value

    @property
    def pos(self):
        return self.__pos

    @pos.setter
    def pos(self, value):
        self.__pos = value

    @property
    def correctPrefixes(self):
        return self.__correctPrefixes

    @correctPrefixes.setter
    def correctPrefixes(self, value):
        self.__correctPrefixes = value

    @property
    def correctSuffixes(self):
        return self.__correctSuffixes

    @correctSuffixes.setter
    def correctSuffixes(self, value):
        self.__correctSuffixes = value
