#!/usr/bin/env python3

# @Author: shubham
# @Date:   2016-04-25 20:10:48
# @Last Modified by:   shubham.chandel
# @Last Modified time: 2016-07-16 22:19:25

from sys import stdin
from json import loads 
from nltk import word_tokenize
from nltk.tag import StanfordNERTagger

frequency = 1
listOfListOfWords = []

# for each line from stdin
for line in stdin:
	try:
		# load json-tweet
		tweet = loads(line)
		tweetText = tweet['text']
		
		# tokenize tweet-text
		listOfWords = word_tokenize(tweetText)
		listOfListOfWords.append(listOfWords)
	
	except:
		pass

# StandfordNER Instance 
nerClf = StanfordNERTagger('english.all.3class.distsim.crf.ser.gz')
nerPair = nerClf.tag_sents(listOfListOfWords)

# word is location and greater than 2 character
locations = []
for ner in nerPair:
	for word, nerType in ner:
		if nerType == 'LOCATION' and len(word) > 2:
			locations.append(word.lower())

for location in locations:
	print((location, frequency))


