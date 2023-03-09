import nltk

class Tag:

	# add pos tags to word
	def addPosTag(self, text):
		posTagged = nltk.pos_tag(text)
		return posTagged

    # get pos tag
	def getPosTag(self, word):
		return nltk.pos_tag([word])