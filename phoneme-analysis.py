#get word containing s and phrase containing that word
# def getInput(callback, callbacksCallback) :
# 	wordInput = 'za_s_'
# 	phraseInput = 'mid zas ya en'
# 	#call findPositions
# 	return callback(wordInput, phraseInput, callbacksCallback)

#find which word and which s we are looking at
# def findPositions(wordInput, phraseInput, callback) :
# 	sWordPosition = wordInput.find('_')
# 	word = wordInput[:sWordPosition] + 's' + wordInput[sWordPosition+3:]
# 	phrase = phraseInput
# 	wordPosition = phrase.find(word)
# 	sPhrasePosition = wordPosition + sWordPosition
# 	#determine syllable after the s, by calling codeSylls
# 	return phrase, word, sWordPosition, callback(phrase, sPhrasePosition, True)

# def codeSylls(phrase, sPhrasePosition, isByS) :
# 	#set up types of syllables
# 	consonants = set(['b', 'c', 'd', 'f', 'g', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z'])
# 	vowels = set(['a', 'e', 'i', 'o', 'u'])
# 	#codes = {'c':'consonant', 'v':'vowel', 'p':'pause', 'i':'intervocalic'}
# 	#what category is the syllable in question, 'syl'?
# 	syl = phrase[sPhrasePosition+1]
# 	if syl != ' ' and isByS:
# 		code = 'i'
# 	else:
# 		syl = phrase[sPhrasePosition+2]
# 		if syl == 'h':
# 			code = 'v'
# 			sPhrasePosition += 1
# 			syl = phrase[sPhrasePosition+3]
# 		elif syl == '#':
# 			code = 'p'
# 		elif syl in consonants:
# 			if syl == 'y':
# 				if phrase[sPhrasePosition+3] == ' ':
# 					code = 'v'
# 				else:
# 					code = 'c'
# 			elif syl == 'c':
# 				nxt = phrase[sPhrasePosition + 3]
# 				if nxt == 'h':
# 					syl = 'C'
# 				code = 'c'
# 			elif syl == 'j':
# 				syl = 'h'
# 				code = 'c'
# 			else:
# 				code = 'c'
# 		elif syl in vowels:
# 			code = 'v'
# 		else:
# 			code = '"uh oh, what is this?!"'
# 	return [syl, code]

# #determine number of syllables in word
# def findNumOfSylls(word) :
# 	wordLength = len(word)
# 	if wordLength <= 2:
# 		sylls = 'mono'
# 	elif wordLength >= 5:
# 		sylls = 'poly'
# 	else:
# 		sylls = codeSylls(word, -2, False)
# 	return sylls


# def report(phrase, word, sWordPosition, nextSyl) :
# 	codes = {'c':'consonant', 'v':'vowel', 'p':'pause', 'i':'intervocalic'}
# 	print('Phrase "{}" contains an "s" as the {}th letter of the word "{}".'.format(phrase, str(sWordPosition+1), word))
# 	print('This "s" is followed by "{}", which is a {}.'.format(nextSyl[0], codes[nextSyl[1]]))
# 	print(nextSyl)

def main() :
	info = getInput(findPositions, codeSylls)
	report(info[0], info[1], info[2], info[3])

main()



