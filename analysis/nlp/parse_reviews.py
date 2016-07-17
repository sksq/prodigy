# -*- coding: utf-8 -*-
# @Author: shubham.chandel
# @Date:   2016-07-16 16:53:21
# @Last Modified by:   shubham.chandel
# @Last Modified time: 2016-07-17 10:59:49

from pprint import pprint
from string import punctuation
from random import shuffle

import rake

import numpy as np
import pandas as pd

from gensim import utils
from gensim.models.doc2vec import LabeledSentence
from gensim.models import Doc2Vec
from gensim.models import Word2Vec
from gensim.models import Phrases

from textblob import TextBlob
from nltk.corpus import stopwords

from havenondemand.hodclient import *

API_KEY = "3f474e8f-4d2d-4556-a171-5bc5d50b4774"

translator = str.maketrans({key: None for key in punctuation})
stop = set(word.strip() for word in open('SmartStoplist.txt'))
client = HODClient(API_KEY, version="v1")

def normalize_text(line):
	# return [word.lower() for word in line.translate(translator).split()]
	return [word.lower() for word in line.translate(translator).split() if word.lower() not in stop]




# swappy2 = []
# for _, row in df.iterrows():
# 	restaurant = row['name']
# 	coordinates = row['lat_long']
# 	topics  = row['topics']
# 	for review in row['reviews']:
# 		tb = TextBlob(review['text'])
# 		for sentence in tb.sentences:
# 			entry = {}
# 			entry['restaurant'] = restaurant
# 			entry['phrase'] = sentence.raw
# 			entry['user-rating'] = review['rating'][6:]
# 			entry['topics'] = topics
# 			entry['feature'] = None 
# 			entry['adj'] = []
# 			entry['sentiment-score'] = sentence.polarity
# 			entry['parentText'] = tb.raw
# 			entry['timestamp'] = review['timestamp']
# 			entry['latitude'] = coordinates.split(',')[0]
# 			entry['longitude'] = coordinates.split(',')[1]
# 			entry['source'] = 'zomato'
# 			swappy2.append(entry)


swappy2 = []
file = 'data_bars.json'

data_frame2 = pd.read_json(file)
for _, row in data_frame2.iterrows():
	restaurant = row['name']
	coordinates = row['lat_long'][35:]
	topics  = row['topics']
	for idx, review in enumerate(row['reviews']):
		tb = TextBlob(review['text'])
		entry = {}
		entry['idx'] = idx
		entry['restaurant'] = restaurant
		# entry['phrase'] = tb.raw
		entry['user-rating'] = float(review['rating'][6:])
		entry['topics'] = topics
		entry['feature'] = None 
		entry['adj'] = []
		entry['sentiment-score'] = tb.polarity
		entry['parentText'] = tb.raw
		entry['timestamp'] = review['timestamp']
		entry['latitude'] = coordinates.split(',')[0]
		entry['longitude'] = coordinates.split(',')[1]
		entry['source'] = 'zomato'
		entry['score'] = entry['user-rating']/5 + entry['sentiment-score']
		swappy2.append(entry)




df = pd.DataFrame(swappy2)
df['timestamp'] = pd.to_datetime(df['timestamp'])

a = df.groupby('restaurant').get_group('Truffles').groupby(df['timestamp'].map(lambda x: x.weekofyear)).mean()['score'].interpolate(method='cubic').plot()
b = df.groupby('restaurant').get_group('Empire Restaurant').groupby(df['timestamp'].map(lambda x: x.weekofyear)).mean()['score'].interpolate(method='cubic').plot()
plt.show(0)



# HPE
responses = []
cnt = 0
for _, row in data_frame2.iterrows():
	for text in row['reviews']:
		try:
			response = client.get_request({'text': text}, HODApps.ANALYZE_SENTIMENT, async=False)
			responses.append(response)
		except:
			break
		cnt += 1
		print(cnt)



# for res in responses:
# 	try:
# 		for review in res['positive']:
# 			if any(word in food and word not in stop for word in review['original_text'].lower().split()):
# 				pprint(review)
# 		for review in res['negative']:
# 			if any(word in food and word not in stop for word in review['original_text'].lower().split()):
# 				pprint(review)
# 	except: continue



swappy2 = []
file = 'data2.json'
cnt = 0

food = set(word.strip().lower() for word in open('fooddb.csv') if word not in stop)
ambiance = set(['ambiance','atmosphere','feel'])
service = set(['service', 'wait', 'waiter', 'queue'])
value = set(['value', 'cost', 'cheap', 'costly', 'pocket', 'price'])

data_frame2 = pd.read_json(file)
idx = 0
for _, row in data_frame2.iterrows():
	restaurant = row['name']
	coordinates = row['lat_long'][35:]
	topics  = row['topics']
	for review in row['reviews']:
		text = review['text']
		response = responses[idx]
		if not response: 
			cnt += 1
			continue
		idx += 1
		for blah1 in response['positive']:
			if any(word in food for word in blah1['original_text'].lower().split() if word not in stop):
				feature = 'Food'
			elif any(word in ambiance for word in blah1['original_text'].lower().split() if word not in stop):
				feature = 'Ambiance'
			elif any(word in service for word in blah1['original_text'].lower().split() if word not in stop):
				feature = 'Service'
			elif any(word in value for word in blah1['original_text'].lower().split() if word not in stop):
				feature = 'Value'	
			else:
				feature = None
			entry = {}
			entry['restaurant'] = restaurant
			entry['user_rating'] = float(review['rating'][6:])
			entry['topics'] = topics
			entry['parent_text'] = text
			entry['parent_score'] = float(response['aggregate']['score'])
			entry['timestamp'] = review['timestamp']
			entry['latitude'] = coordinates.split(',')[0]
			entry['longitude'] = coordinates.split(',')[1]
			entry['source'] = 'zomato'
			entry['phrase'] = blah1['original_text']
			entry['feature'] = feature
			entry['adj'] = []
			entry['sentiment_score'] = float(blah1['score'])
			entry['score'] = (entry['sentiment_score'] + 1)/2 + entry['user_rating']/5
			swappy2.append(entry)
		for blah2 in response['negative']:
			if any(word in food for word in blah2['original_text'].lower().split() if word not in stop):
				feature = 'Food'
			elif any(word in ambiance for word in blah1['original_text'].lower().split() if word not in stop):
				feature = 'Ambiance'
			elif any(word in service for word in blah1['original_text'].lower().split() if word not in stop):
				feature = 'Service'
			elif any(word in value for word in blah1['original_text'].lower().split() if word not in stop):
				feature = 'Value'
			else:	
				feature = None
			entry = {}
			entry['restaurant'] = restaurant
			entry['user_rating'] = float(review['rating'][6:])
			entry['topics'] = topics
			entry['parent_text'] = text
			entry['parent_score'] = float(response['aggregate']['score'])
			entry['timestamp'] = review['timestamp']
			entry['latitude'] = coordinates.split(',')[0]
			entry['longitude'] = coordinates.split(',')[1]
			entry['source'] = 'zomato'
			entry['phrase'] = blah2['original_text']
			entry['feature'] = feature
			entry['adj'] = []
			entry['sentiment_score'] = float(blah2['score'])
			entry['score'] = (entry['sentiment_score'] + 1)/2 + entry['user_rating']/5
			swappy2.append(entry)


# W2V
data_frame2 = pd.read_json('truffles1.txt')
all_reviews = []
for _, row in data_frame2.iterrows():
	all_reviews.append(row['reviews']['text'])

all_reviews = pd.Series(all_reviews)
sentences = all_reviews.apply(normalize_text)
bigram_transformer = Phrases(sentences)
model = Word2Vec(bigram_transformer[sentences], size=1000, min_count=10)

# RAKE
# text = ' | '.join(all_reviews) 
# rake_object = rake.Rake("SmartStoplist.txt", 3, 1, 10)
# keywords = rake_object.run(text)



