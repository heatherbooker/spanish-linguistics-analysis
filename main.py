def main() :
	from phraseClass import Speech
	from reporterClass import Reporter
	from linguistClass import Linguist
	speech = Speech('za_s_', 'mid zas ya en')
	reporter = Reporter()
	linguist = Linguist(speech.getPhrase(), speech.getWord())
	reporter.report(speech.getPhrase(), speech.getWord(), speech.getSPhrasePos(), linguist.getNextSyl())

main()
