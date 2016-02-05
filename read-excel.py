#get word containing s and phrase containing that word
def getInput(callback, callbacksCallback) :
	wordInput = 'za_s_'
	phraseInput = 'mid zas ya en'
	#call findPositions
	return callback(wordInput, phraseInput, callbacksCallback)