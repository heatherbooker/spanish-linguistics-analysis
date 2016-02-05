class Reporter():

	def __init__(self):
		self.codes = {'c':'consonant', 'v':'vowel', 'p':'pause', 'i':'intervocalic'}

	def report(self, phrase, word, sWordPosition, nextSyl) :
		print('Phrase "{}" contains an "s" as the {}th letter of the word "{}".'.format(phrase, str(sWordPosition+1), word))
		print('This "s" is followed by "{}", which is a {}.'.format(nextSyl[0], self.codes[nextSyl[1]]))

#should there be a new instance of reporter every time a word/phrase is processed? or just have 
#a method report and take args?

reporter = Reporter()
reporter.report('gsdfgsfd', 'sdf', 0, ['p','p'])