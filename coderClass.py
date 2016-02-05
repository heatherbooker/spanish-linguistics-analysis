class Coder():
	#find which word and which s we are looking at
	def findPositions(wordInput, phraseInput, callback) :
		sWordPosition = wordInput.find('_')
		word = wordInput[:sWordPosition] + 's' + wordInput[sWordPosition+3:]
		phrase = phraseInput
		wordPosition = phrase.find(word)
		sPhrasePosition = wordPosition + sWordPosition
		#determine syllable after the s, by calling codeSylls
		return phrase, word, sWordPosition, callback(phrase, sPhrasePosition, True)