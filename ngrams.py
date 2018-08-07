from sklearn.feature_extraction.text import CountVectorizer
import pickle

with open("/Users/eunseo/Desktop/countries/cat_tokens_countries2_2.txt", "r") as f:
	my_doc = f.read()

documents = [my_doc]
new_regex = r"(?u)\b\w+\b"
example_vectorizer = CountVectorizer(token_pattern=new_regex) #initialize your count vectorizer
example_vectorizer.fit(documents) #documents much be a vector of strings(individual documents)
pickle.dump(example_vectorizer, open("/Users/eunseo/Desktop/countries/vector_vocab", "wb"))
X = example_vectorizer.transform(documents).toarray()
pickle.dump(X, open("/Users/eunseo/Desktop/countries/vector_matrix", "wb"))



