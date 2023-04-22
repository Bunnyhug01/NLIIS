import nltk
from nltk.corpus import wordnet
from nltk.tree import *

from textPreprocessing import textPreprocessing


class SemanticTree:
    
    def generateTree(self, text):
        text = text.replace('\n', '')

        if text != '':

            result = '(S '
            sentences = nltk.sent_tokenize(text)
            for sentence in sentences:

                resultSentence = '(SENT '
                words = textPreprocessing(sentence)
                for word in words:
                    
                    if word.isalpha():
                        resultSentence += self.getWordSemantic(word) + ' '

                resultSentence += ')'
                result += resultSentence

            result += ')'
            return nltk.tree.Tree.fromstring(result)


    def getWordSemantic(self, word):
        if len(wordnet.synsets(word)) == 0:
            return '(WS (W ' + word + '))'
        
        result = '(WS (W ' + word + ') (DEF ' + wordnet.synsets(word)[0].definition() + ')'

        word = wordnet.synsets(word)

        synonyms = getSynonyms(word)
        antonyms = getAntonyms(word)
        hyponyms = getHyponyms(word)
        hypernyms = getHypernyms(word)

        result = self.addWordsToTree(synonyms, result, ' (SYN ')
        result = self.addWordsToTree(antonyms, result, ') (ANT ')
        result = self.addWordsToTree(hyponyms, result, ') (HY ')
        result = self.addWordsToTree(hypernyms, result, ') (HE ')

        result += '))'
        return result


    def addWordsToTree(self, words, result, type: str):
        if len(words):
            result += type
            for word in words:
                result += word + ' '
        return result      


    def drawTree(self, tree):
        # Convert tree to text
        return TreePrettyPrinter(tree).text()


def getSynonyms(word):
    synonyms = []
    for synset in word:
        for lemma in synset.lemmas():
            synonyms.append(lemma.name())
    return synonyms


def getSynonymsString(word):
    synonyms = []
    for synset in wordnet.synsets(word):
        for lemma in synset.lemmas():
            synonyms.append(lemma.name())
            
    synonyms.append(word)
    return synonyms


def getAntonyms(word):
    antonyms = []
    for synset in word:
        for lemma in synset.lemmas():
            if lemma.antonyms():
                antonyms.append(lemma.antonyms()[0].name())
    return antonyms


def getHyponyms(word):
    hyponyms = []
    for hyponym in word[0].hyponyms():
        hyponyms.append(hyponym.name())
    return hyponyms


def getHypernyms(word):
    hypernyms = []
    for hypernym in word[0].hypernyms():
        hypernyms.append(hypernym.name())
    return hypernyms