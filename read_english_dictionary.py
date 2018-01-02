import json
import os, sys

def load_words():
	try:
		filename = "words_dictionary.json"
		with open(filename,"r") as english_dictionary:
			valid_words = json.load(english_dictionary)
			print("dictionary loaded")
			return valid_words
	except Exception as e:
		print("dict load failed")
		return str(e)

if __name__ == '__main__':
	english_words = load_words()
	# demo print
	print(str(english_words["fate"]))
