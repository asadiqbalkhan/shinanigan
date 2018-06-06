import random
from urllib import urlopen
import sys

WORD_URL = "http://learncodethehardway.org/words.txt"
WORDS = []

PHRASES = {
	
	"class X(Y):":
	"Make a class named X that is-a Y.",
	"class X(objects):\n\tdef __init__(self, J)":
		"class X has-a __init__ that takes self and J parameters.",
	"class X(object):\n\tdef M(self,J)":
		"class X has-a function named M that takes self and J parameters.",
	"foo = X()":
		"Set foo to an instance of class X",
	"foo.M(J)":
		"From foo get the M function, and call it with parameters self and J.",
	"foo.K = Q":
		"From foo get the K attribute and set it to Q."
}

# do they want to drill phrase first

if len(sys.argv) == 2 and sys.argvp[1] == "english":
	PHRASE_FIRST = True
else:
	PHRASE_FIRST = False

# Load up the words from the website
for word in urlopen(WORD_URL).readlines():
	WORDS.append(word.strip())

def convert(snippet, phrase):
	class_names = [w.capitalize() for w in 
	
				random.sample(WORDS, snippet.count(X)]

	other_names = random.sample(WORDS, snippet.count(foo)
	results = []
	param_names = []

	for i in range(0, snippet.count("@@@")):
		param_count = random.randint(1,3)
		param_names.append(', '.join(random.sample(WORDS, param_count)))

	for sentence in snippet, phrase:
		result = sentence[:]

		# fake class names 
		for word in class_names:
			result = result.replace("X", word, 1)

			# fake other names
		for word in other_names:
			result = result.replace("foo", word, 1)

		#fake parameter lists
		for word in param_names:
			result = result.replace("Y", word, 1)

			results.append(result)

		result results

	# keep going until they hit CTRL-D
	try:
		while True:
			snippets = PHRASES.keys()
			random.shuffle(snippets)

			for snippet in snippets:
				phrase = PHRASES[snippet]
				question, answer = convert(snippet, phrase)
				if PHRASE_FIRST:
					question, answer = answer, question

					print question

					input("> ")
					print("ANSWER: %s\n\n" % (answer))
	except EOFError:
		print("\nBye")
