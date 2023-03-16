
from words import Word

class Affix:
	
    wordForm = Word()

    generalPrefixes = ['anti', 'auto', 'mid', 'post', 'pre', 'super', 'sub', 'de', 'over', 'under', 're', 'en', 'em', 'extra', 'inter']
    negativePrefixes = ['un', 'im', 'in', 'il', 'ir', 'dis', 'mis']

    nounSuffixes = ['er', 'or', 'an', 'ian', 'ist', 'ant', 'ent', 'ee', 'ess', 'ity', 'ance', 'ence', 'ancy', 'ency',
                    'ism', 'hood', 'ure', 'ion', 'tion', 'sion', 'dom', 'ment', 'ness', 'ship', 'th']
    adjectiveSuffixes = ['ful', 'less', 'able', 'ous', 'y', 'al', 'ar', 'ant', 'ent', 'ary', 'ory', 'ic', 'ive', 'ish', 'long']
    verbSuffixes = ['ate', 'ify', 'fy', 'ise', 'ize', 'en', 'ish']
    adverbSuffixes = ['ly', 'wise', 'ward', 'wards']

    def addPrefix(self, word, prefix):
        newWord = ''
        newWord += prefix + word
        return newWord

    def addSuffix(self, word, suffix):
        newWord = ''
        newWord += word + suffix
        return newWord

    def getPrefixes(self, word, prefixes):
        correctPrefixes = []
        for prefix in prefixes:
            if self.wordForm.checkWord(self.addPrefix(word, prefix)):
                correctPrefixes.append(prefix)
        return correctPrefixes

    def getSuffixes(self, word, suffixes):
        correctSuffixes = []
        for suffix in suffixes:
            if self.wordForm.checkWord(self.addSuffix(word, suffix)):
                correctSuffixes.append(suffix)
        return correctSuffixes