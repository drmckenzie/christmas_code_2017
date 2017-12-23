# using the dictionary (small.txt) from here:
# -- http://phillipmfeldman.org/English/spelling%20dictionaries.html
# specially designed for a small dataset 15000 words (kid-friendly)
#
# Alternate dictionary here, with 1000 words (top_1000_english_words.txt):
# -- https://www.ef.co.uk/english-resources/english-vocabulary/top-1000-words/

# do the imports
import sys # for file access

# specify dictionary file:
dictionary_file= 'top_1000_english_words.txt'

# read the dictionary file:
with open(dictionary_file,'r') as FILE:
	words= [ word.rstrip() for word in FILE]
	
print(words[0:10])
