# -*- coding: utf-8 -*-
# @Author: shubham.chandel
# @Date:   2016-07-16 22:27:08
# @Last Modified by:   shubham.chandel
# @Last Modified time: 2016-07-16 22:56:20

from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.decomposition import NMF, LatentDirichletAllocation
from sklearn.datasets import fetch_20newsgroups

n_features = 2000
n_topics = 10
n_top_words = 5


def print_top_words(model, feature_names, n_top_words):
	for topic_idx, topic in enumerate(model.components_):
			print("Topic #%d:" % topic_idx)
			print(" ".join([feature_names[i] for i in topic.argsort()[:-n_top_words - 1:-1]]))
	print()


# dataset = fetch_20newsgroups(shuffle=True, random_state=1, remove=('headers', 'footers', 'quotes'))
# data_samples = dataset.data


df = pd.read_json('data.json')
df.lat_long = df.lat_long.apply(lambda x: x[35:])

data_samples = []
for reviews in df.reviews:
	for review in reviews:
		data_samples.append(review['text'])

data_samples = pd.Series(data_samples)

tfidf_vectorizer = TfidfVectorizer(max_df=0.95, min_df=2, stop_words='english')
tfidf = tfidf_vectorizer.fit_transform(data_samples)

tf_vectorizer = CountVectorizer(max_df=0.95, min_df=2, max_features=n_features, stop_words='english')
tf = tf_vectorizer.fit_transform(data_samples)

nmf = NMF(n_components=n_topics, random_state=1, alpha=.1, l1_ratio=.5).fit(tfidf)

tfidf_feature_names = tfidf_vectorizer.get_feature_names()
print_top_words(nmf, tfidf_feature_names, n_top_words)

lda = LatentDirichletAllocation(n_topics=n_topics, max_iter=5, learning_method='online', learning_offset=50., random_state=0)
lda.fit(tf)

tf_feature_names = tf_vectorizer.get_feature_names()
print_top_words(lda, tf_feature_names, n_top_words)


