import nltk
import re
import pprint
from nltk import Tree

sample_text = """Good behavior upon the street, or public promenade, marks the gentleman
most effectually; rudeness, incivility, disregard of "what the world
says," marks the person of low breeding. We always know, in walking a
square with a man, if he is a gentleman or not. A real gentility never
does the following things on the street, in presence of observers:--

Never picks the teeth, nor scratches the head.

Never swears or talks uproariously.

Never picks the nose with the finger.

Never smokes, or spits upon the walk, to the exceeding annoyance of
those who are always disgusted with tobacco in any shape.

Never stares at any one, man or woman, in a marked manner.

Never scans a lady's dress impertinently, and makes no rude remarks
about her.

Never crowds before promenaders in a rough or hurried way.

Never jostles a lady or gentleman without an "excuse me."

Never treads upon a lady's dress without begging pardon.

Never loses temper, nor attracts attention by excited conversation.

Never dresses in an odd or singular manner, so as to create remark.

Never fails to raise his hat politely to a lady acquaintance; nor to
a male friend who may be walking with a lady--it is a courtesy to the
lady.
"""

grammar = r"""
  NP: {<DT|JJ|NN.*>+}          # Chunk sequences of DT, JJ, NN
  PP: {<IN><NP>}               # Chunk prepositions followed by NP
  VP: {<VB.*><NP|PP|CLAUSE>+$} # Chunk verbs and their arguments
  CLAUSE: {<NP><VP>}           # Chunk NP, VP
  """
NPChunker = nltk.RegexpParser(grammar)

def prepare_text(input):
	sentences = nltk.sent_tokenize(input)
	sentences = [nltk.word_tokenize(sent) for sent in sentences]
	sentences = [nltk.pos_tag(sent) for sent in sentences]
	sentences = [NPChunker.parse(sent) for sent in sentences]
	return sentences


def parsed_text_to_NP(sentences):
	nps = []
	for sent in sentences:
		tree = NPChunker.parse(sent)
		for subtree in tree.subtrees():
			if subtree.label() == 'NP':
				t = subtree
				t = ' '.join(word for word, tag in t.leaves())
				nps.append(t)
	return nps


def sent_parse(input):
	sentences = prepare_text(input)
	nps = parsed_text_to_NP(sentences)
	return nps

def find_nps(text):
	prepared = prepare_text(text)
	parsed = parsed_text_to_NP(prepared)
	final = sent_parse(parsed)


parsed_text_to_NP(prepare_text(sample_text))



