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
	return phrase, word, sPhrasePosition, callback(phrase, sPhrasePosition)

#set up types of syllables(consonant, vowel, pause, otherCat#######!!!!!!!!!!!!!)
consonants = set(['b', 'd', 'f', 'g', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'z'])
vowels = set(['a', 'e', 'i', 'o', 'u'])
y = 'y'
h = 'h'

#determine syllables surrounding the s
def codeSylls(phrase, sPhrasePosition) :
	nextSyl = phrase[sPhrasePosition+1]
	prevSyl = phrase[sPhrasePosition-1]
	for syl in (nextSyl, prevSyl):
		if syl == ' ':
			syl = phrase[sPhrasePosition+2]
			if syl == '#':
				prevSylType = 'pause'
			elif syl == 'h':
				syl = phrase[sPhrasePosition+3]
			if syl == 'c':
				if 
			if syl in consonants:
				prevSylType = 'consonant'
			elif syl in vowels:
				prevSylType = 'vowel'
		else:
			prevSylType = 'intervocalic'
		if 'nextSylType' not in locals():
			nextSylType = prevSylType
	return [nextSyl, nextSylType, prevSyl, prevSylType]


def report(phrase, word, sWordPosition, nxAnPrvSyls) :
	print('Phrase "' + phrase + '" contains an "s" as the ' + str(sWordPosition+1) + 'th letter of the word "{}".'.format(word))
	print('This "s" is followed by "{}", which is a {}, and preceeded by "{}", which is a {}.'.format(nxAnPrvSyls[0], nxAnPrvSyls[1], nxAnPrvSyls[2], nxAnPrvSyls[3]))

def main() :
	info = getInput(findPositions, codeSylls)
	report(info[0], info[1], info[2], info[3])

main()


