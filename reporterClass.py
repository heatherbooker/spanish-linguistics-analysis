class Reporter():
	def report(phrase, word, sWordPosition, nextSyl) :
		codes = {'c':'consonant', 'v':'vowel', 'p':'pause', 'i':'intervocalic'}
		print('Phrase "{}" contains an "s" as the {}th letter of the word "{}".'.format(phrase, str(sWordPosition+1), word))
		print('This "s" is followed by "{}", which is a {}.'.format(nextSyl[0], codes[nextSyl[1]]))
		print(nextSyl)

#should there be a new instance of reporter every time a word/phrase is processed? or just have 
#a method report and take args?