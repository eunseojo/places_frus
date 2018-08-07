

import pickle
import re

sorted_locations = pickle.load(open("/Users/eunseo/Desktop/countries/sorted_places", "rb"))
catted_doc = open("/Users/eunseo/Desktop/cat_tokens_countries.txt", "r")

catted_str = catted_doc.read()
catted_doc.close()

for loc in sorted_locations:
	pattern = "\s" + loc[0] + "\s"
	repl = " " + loc[1] + " "
	catted_str = re.sub(pattern, repl, catted_str)
	print(loc)
	

with open("/Users/eunseo/Desktop/cat_tokens_countries2.txt", "w") as f:
	f.write(catted_str)
