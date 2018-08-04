import pickle

with open("./nations_cognates.txt","r") as f:
	ff = f.read()

q = ff.split("\n")


multi = {}

multi_4 = []
multi_3 = []
multi_2 = []
single = []

def print_repeat(country, unique):
	if country in unique:
		print(country)
	else:
		unique.add(country)

def allocate(no_words, nation, label):
	tup = (nation, label, len(nation))    
	if no_words == 1:
		single.append(tup)
	elif no_words ==2:
		multi_2.append(tup)
	elif no_words == 3:
		multi_3.append(tup)
	elif no_words == 4:
		multi_4.append(tup)

for item in q:
	li = item.split(", ")
	if len(li) > 1:
		label = "00_" + "".join(li[0].split(" "))
		multi[label] = li
		for nation in li:
			n_split = nation.split()
			no_words = len(n_split)
			allocate(no_words, nation, label)

ordered = []

ordered.extend(sorted(multi_4, key=lambda x: x[2], reverse=True))
ordered.extend(sorted(multi_3, key=lambda x: x[2], reverse=True))
ordered.extend(sorted(multi_2, key=lambda x: x[2], reverse=True))
ordered.extend(sorted(single, key=lambda x: x[2], reverse=True))


pickle.dump(ordered, open("./sorted_places", "wb"))

#order: 1. Multiple token words, 2. Longest characters

