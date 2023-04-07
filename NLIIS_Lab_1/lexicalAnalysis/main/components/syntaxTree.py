from textPreprocessing import textPreprocessing
from tags import Tag

from nltk import RegexpParser
from nltk.tree.prettyprinter import TreePrettyPrinter


class SyntaxTree:
    tag = Tag()

    def generateTree(self, sentence):

        sentence = textPreprocessing(sentence)
        tagged = self.tag.addPosTag(sentence)

        # Extract all parts of speech from any text
        chunker = RegexpParser("""
                            NP: {<DT>?<JJ>*<NN>}    #To extract Noun Phrases
                            P: {<IN>}               #To extract Prepositions
                            V: {<V.*>}              #To extract Verbs
                            PP: {<P> <NP>}          #To extract Prepositional Phrases
                            VP: {<V> <NP|PP>*}      #To extract Verb Phrases
                            """)

        # Print all parts of speech in above sentence
        output = chunker.parse(tagged)

        return output

    
    def drawTree(self, tree):
        # Convert tree to text
        return TreePrettyPrinter(tree).text()