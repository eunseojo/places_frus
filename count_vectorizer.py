from sklearn.feature_extraction.text import CountVectorizer
import pickle
import matplotlib.pyplot as plt
import numpy as np


v = pickle.load(open("/Users/eunseo/Desktop/countries/vector_vocab", "rb"))
X = pickle.load(open("/Users/eunseo/Desktop/countries/vector_matrix", "rb"))
vocab = v.vocabulary_

locations = []

for k,v in vocab.items():
	if k[:3] == "00_":
		locations.append((k, X[0,v]))

sort_vocab = sorted(locations, key=lambda x: x[1], reverse=True)

x,y = zip(*sort_vocab)
x = np.arange(len(x))


plt.scatter(x,y)
plt.show()