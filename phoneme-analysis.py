#get word containing s and phrase containing that word
def getInput(callback, callbacksCallback) :
	wordInput = 'za_s_r'
	phraseInput = 'mid zasr en'
	return callback(wordInput, phraseInput, callbacksCallback)

#find which word and which s we are looking at
def findPositions(wordInput, phraseInput, callback) :
	sWordPosition = wordInput.find('_')
	word = wordInput[:sWordPosition] + 's' + wordInput[sWordPosition+3:]
	phrase = phraseInput
	wordPosition = phrase.find(word)
	sPhrasePosition = wordPosition + sWordPosition
	return phrase, word, sWordPosition, callback(phrase, sPhrasePosition)

#determine number of syllables in word
def findNumOfSylls() :
	wordLength = len(word)
	if wordLength <= 2:
		sylls = 'mono'
	elif wordLength >= 5:
		sylls = 'poly'
	else:
		sylls = 'idk???'


#determine syllable after the s
def codeSylls(phrase, sPhrasePosition) :
	#set up types of syllables
	consonants = set(['b', 'd', 'f', 'g', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'z'])
	vowels = set(['a', 'e', 'i', 'o', 'u'])
	codes = {'c':'consonant', 'v':'vowel', 'p':'pause', 'i':'intervocalic'}
	#where does nextSyl belong?
	nextSyl = phrase[sPhrasePosition+1]
	if nextSyl != ' ':
		code = 'i'
	else:
		nextSyl = phrase[sPhrasePosition+2]
		if nextSyl == 'y':
			if phrase[sPhrasePosition+3] == ' ':
				code = 'v'
			else:
				code = 'c'
		if nextSyl == 'h':
			code = 'v'
			positn = sPhrasePosition + 1
		if nextSyl == 'c':
			if 'positn' in locals():
				nxt = phrase[positn + 3]
			else:
				nxt = phrase[sPhrasePosition + 3]
			if nxt == 'h':
				nextSyl = 'C'
			code = 'c'
		if nextSyl == '#':
			code = 'p'
		elif nextSyl in consonants:
			code = 'c'
		elif nextSyl in vowels:
			code = 'v'
	return [nextSyl, code]


def report(phrase, word, sWordPosition, nextSyl) :
	print('Phrase {} contains an "s" as the {}th letter of the word "{}".'.format(phrase, str(sWordPosition+1), word))
	print('This "s" is followed by "{}", which is a {}.'.format(nextSyl[0], nextSyl[1]))

def main() :
	info = getInput(findPositions, codeSylls)
	report(info[0], info[1], info[2], info[3])

main()



