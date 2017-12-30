# Importing the wordsearch (assume it's a rectangle!)

# do the imports
import sys # for file access
import my_split # for splitting strings by multiple delimiters
import generate_word_arrays # for generating lists of words from a line.

# my_split notes:
# print(my_split.my_split('1111  2222 3333;4444,5555;6666', [' ', ';', ',']))

# specify wordsearch file:
wordsearch_file= 'wordsearch_test_1.txt'
wordsearch_file= 'wordsearch_test_2.txt'
wordsearch_file= 'wordsearch_test_3.txt'

# specify dictionary file:
dictionary_file= 'top_1000_english_words.txt'
dictionary_file= 'small.txt'

# specify delimiters
multipleDelimiters= [' ', ';', ',', '.', '-', '=', '<', '>', '*', '/', '\\', '_', '[', ']']

f = open(wordsearch_file,'r')
nLines= 0
nCols= 0
strWordsearch= []
for line in iter(f):
	strWordsearch.append(line.rstrip().lower())
	nLines += 1
	if ( nCols == 0 ):
		nCols= len(line.rstrip().lower())
	else:
		if ( nCols != len(line.rstrip().lower()) ):
			print("something strange went on here.")
			
f.close()

strWordsearchTrans= ["x"  for x in range(nCols)]
print(len(strWordsearchTrans[0]))
for iRow in range(0, nCols):
	strWordsearchTrans[iRow]= [' '  for x in range(nLines)]
	print("." + "".join(["x"  for x in range(nLines)]) + ".")

# transpose:
for iRow in range(0,nCols):
	tempstr= []
	for iCol in range(0, nLines):
		# ugh, this feels dirty. How do I do this right? #todo
		tempstr.append(strWordsearch[iCol][iRow])
	strWordsearchTrans[iRow]= ''.join(tempstr) 
	# print(strWordsearchTrans[iRow])
	
# wait = input("PRESS ENTER TO CONTINUE.")

# debug
print(strWordsearch[1][2])
print(strWordsearchTrans[2][1])
# wait = input("PRESS ENTER TO CONTINUE.")

# debug
print(strWordsearch[0])
print(strWordsearch[5])
print("No. Lines = " + str(nLines))
print("No. columns = " + str(nCols))

# debug - print rows
for iRow in range(0,nLines):
	print(str(iRow) + " = " + strWordsearch[iRow])

# now generate a list of potential words to search the dictionary:
listOfStringsThatMightBeWords= []
for iRow in range(0,nLines):
	candidates = generate_word_arrays.generate_word_arrays(strWordsearch[iRow])
	for words in candidates:
		listOfStringsThatMightBeWords.append(words)

# do the same with the transposed array:
for iRow in range(0,nCols):
	candidates = generate_word_arrays.generate_word_arrays(strWordsearchTrans[iRow])
	for words in candidates:
		listOfStringsThatMightBeWords.append(words)		
		
print(listOfStringsThatMightBeWords[0:100])
print("Length of candidates list = " + str(len(listOfStringsThatMightBeWords)))

## now for looking up the dictionary.

# import the dictionary as a list:
with open(dictionary_file,'r') as DICTFILE:
	wordsDictionary= [ word.rstrip() for word in DICTFILE]
	wordsDictionaryLen= [ len(word) for word in words]

wordsFound= []
for word in wordsDictionary:
	if word in listOfStringsThatMightBeWords:
		wordsFound.append(word)

print("" + str(len(wordsFound)) +  " words found:")
print(wordsFound)

print("Now do the same for backwards (then figure out diagonals)")