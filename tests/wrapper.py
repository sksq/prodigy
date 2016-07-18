#! /Users/s.sharma/anaconda3/bin/python3
import json, pandas as pd, math
import pickle
from datetime import datetime

fileName = 'swappy'
# with open(fileName) as file:
# 	data = json.load(file)

data = pickle.load(open(fileName, 'rb'))

stops = pd.DataFrame(data)
stops.columns = ['adj', 'feature', 'latitude', 'longitude', 'parent_score',
       'parent_text', 'text', 'restaurant', 'unknown_score', 'score',
       'source', 'timestamp', 'topics', 'user_rating']
stops['timestamp'] = pd.to_datetime(stops['timestamp'])
stops['longitude'] = stops['longitude'].apply(lambda element: float(element))
stops['latitude'] = stops['latitude'].apply(lambda element: float(element))

def dist(x1, y1, x2, y2):
	return math.sqrt(math.pow(x1 - x2, 2) + math.pow(y1 - y2, 2))

def getTextDataOnClick(restaurant, from_time, to_time, sources, feature, maxScore, minScore):
	return stops[(stops['restaurant'] == restaurant) & stops['source'].isin(sources) & (stops['timestamp'] >= from_time) & (stops['timestamp'] <= to_time) & (stops['feature'] == feature) & (stops['score'] >= minScore) & (stops['score'] <= maxScore)]['parent_text']

def getAdj(restaurant, from_time, to_time, sources, feature):
	return stops[(stops['restaurant'] == restaurant) & stops['source'].isin(sources) & (stops['timestamp'] >= from_time) & (stops['timestamp'] <= to_time) & (stops['feature'] == feature)]['adj']

def getFeatures(restaurant, from_time, to_time, sources):
	return stops[(stops['restaurant'] == restaurant) & stops['source'].isin(sources) & (stops['timestamp'] >= from_time) & (stops['timestamp'] <= to_time)]['feature']

def getDataTemporalOr(restaurants, from_time, to_time, sources, feature):
	tempData = stops[stops['restaurant'].isin(restaurants) & stops['source'].isin(sources) & (stops['timestamp'] >= from_time) & (stops['timestamp'] <= to_time) & (stops['feature'] == feature)]

	dict = {}
	for name, group in tempData.groupby('restaurant'):
		subDict = {}
		for subName, subGroup in group.groupby('feature'):
			iList = []
			for row in subGroup.iterrows():
				iList.append(row[1].to_dict())
			subDict[subName] = iList
		dict[name] = subDict

	return dict

def getDataTemporal():
	tempData = stops

	dict = {}
	for name, group in tempData.groupby('restaurant'):
		subDict = {}
		for subName, subGroup in group.groupby('feature'):
			iList = []
			for row in subGroup.iterrows():
				iList.append(row[1].to_dict())
			subDict[subName] = iList
		dict[name] = subDict

	return dict

def getDataGeo(Topics, lat, lon, radius, from_time, to_time, sources, feature):
	return stops[stops['topics'].apply(lambda row:(len(set(row).intersection(set(Topics))) > 0)) & stops.T.apply(lambda row:(dist(lat, lon, row['latitude'], row['longitude']) <= radius)) & stops['source'].isin(sources) & (stops['timestamp'] >= from_time) & (stops['timestamp'] <= to_time) & (stops['feature'] == feature)]
