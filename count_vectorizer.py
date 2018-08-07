from sklearn.feature_extraction.text import CountVectorizer
import pickle


v = pickle.load(open("/Users/eunseo/Desktop/countries/vector_vocab", "rb"))
X = pickle.load(open("/Users/eunseo/Desktop/countries/vector_matrix", "rb"))
vocab = v.vocabulary_

locations = []

for k,v in vocab.items():
	if k[:3] == "00_":
		locations.append((k, X[0,v]))

print(sorted(locations, key=lambda x: x[1], reverse=True))