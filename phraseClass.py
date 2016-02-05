class Speech():
	
	def __init__(self, wordInput, phrase):
		self.sWordPosition = wordInput.find('_')
		self.word = self.extractWord(wordInput)
		self.phrase = phrase
		self.sPhrasePosition = self.extractPos()

	def extractWord(self, wordInput):
		word = wordInput[:self.sWordPosition] + 's' + wordInput[self.sWordPosition+3:]
		return word

	def extractPos(self):
		wordPosition = self.phrase.find(self.word)
		sPhrasePosition = wordPosition + self.sWordPosition
		return sPhrasePosition

	def getWord(self):
		return self.word

	def getPhrase(self):
		return self.phrase

	def getSPhrasePos(self):
		return self.sPhrasePosition

# speech = Speech('za_s_', 'mid zas ya en')

