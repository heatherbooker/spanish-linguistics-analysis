class Linguist() :

	def __init__(self, phrase, word):
		self.phrase = phrase
		self.word = word

	#determine number of syllables in word
	def findNumOfSylls(word) :
		wordLength = len(word)
		if wordLength <= 2:
			sylls = 'mono'
		elif wordLength >= 5:
			sylls = 'poly'
		else:
			sylls = codeSylls(word, -2, False)
		return sylls

	def codeSylls(phrase, sPhrasePosition, isByS) :
		#set up types of syllables
		consonants = set(['b', 'c', 'd', 'f', 'g', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z'])
		vowels = set(['a', 'e', 'i', 'o', 'u'])
		#codes = {'c':'consonant', 'v':'vowel', 'p':'pause', 'i':'intervocalic'}
		#what category is the syllable in question, 'syl'?
		syl = phrase[sPhrasePosition+1]
		if syl != ' ' and isByS:
			code = 'i'
		else:
			syl = phrase[sPhrasePosition+2]
			if syl == 'h':
				code = 'v'
				sPhrasePosition += 1
				syl = phrase[sPhrasePosition+3]
			elif syl == '#':
				code = 'p'
			elif syl in consonants:
				if syl == 'y':
					if phrase[sPhrasePosition+3] == ' ':
						code = 'v'
					else:
						code = 'c'
				elif syl == 'c':
					nxt = phrase[sPhrasePosition + 3]
					if nxt == 'h':
						syl = 'C'
					code = 'c'
				elif syl == 'j':
					syl = 'h'
					code = 'c'
				else:
					code = 'c'
			elif syl in vowels:
				code = 'v'
			else:
				code = '"uh oh, what is this?!"'
		self.nextSyl = syl
		self.nextSylCateg = code

	def getNextSyl(self):
		return self.nextSyl, self.nextSylCateg
	