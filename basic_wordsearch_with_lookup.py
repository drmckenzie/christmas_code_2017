# Importing the wordsearch (assume it's a rectangle!)

# do the imports
import sys # for file access
import my_split # for splitting strings by multiple delimiters
import generate_word_arrays # for generating lists of words from a line.
import generate_diagonal_list # the diagonals.
import os
#sys.path.append('../english-words')
import read_english_dictionary	

# my_split notes:
# print(my_split.my_split('1111  2222 3333;4444,5555;6666', [' ', ';', ',']))

# specify wordsearch file:
wordsearch_file= 'wordsearch_test_1.txt'
wordsearch_file= 'wordsearch_test_2.txt'
#wordsearch_file= 'wordsearch_test_3.txt'
wordsearch_file= 'wordsearch_test_4.txt'

# specify dictionary file:
dictionary_file= 'top_1000_english_words.txt'
dictionary_file= 'small.txt'
dictionary_file= '..\english-words\words_alpha.txt'

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

# make a transposed array. First, make a dummy array. (there is probably an easier way)
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

# reverse the array
strWordsearchReversed= []
for iRow in range(0,nLines):
	strWordsearchReversed.append(strWordsearch[iRow][::-1])
	
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

# now add the diagonals. First with the normal wordsearch:
diagonalFrontWords = generate_diagonal_list.generate_diagonal_list(strWordsearch)
for iWord in range(0,len(diagonalFrontWords)):
	listOfStringsThatMightBeWords.append(diagonalFrontWords[iWord])		
print("Diagonal front words")
print(diagonalFrontWords)

# and now with the reversed grid:
diagonalReversedWords = generate_diagonal_list.generate_diagonal_list(strWordsearchReversed)
for iWord in range(0,len(diagonalReversedWords)):
	listOfStringsThatMightBeWords.append(diagonalReversedWords[iWord])		
print("Diagonal reversed words")
print(diagonalReversedWords)

# Now add every string, but backwards (double the word list) 
for iWord in range(0,len(listOfStringsThatMightBeWords)):
	thisWord = listOfStringsThatMightBeWords[iWord]
	# print(thisWord + " " + thisWord[::-1])
	listOfStringsThatMightBeWords.append(thisWord[::-1])

# print(listOfStringsThatMightBeWords)
	
# make sure it's unique:
listOfStringsThatMightBeWords = list(set(listOfStringsThatMightBeWords))	

# debug
print(listOfStringsThatMightBeWords[0:100])
print("Length of candidates list = " + str(len(listOfStringsThatMightBeWords)))
	
## now for looking up the dictionary.

# import the dictionary as a list:
with open(dictionary_file,'r') as DICTFILE:
	wordsDictionary= [ word.rstrip() for word in DICTFILE]
	wordsDictionaryLen= [ len(word) for word in words]

wordsFound= []
# slow lookup:
#for word in wordsDictionary:
#	if word in listOfStringsThatMightBeWords:
#		wordsFound.append(word)

# faster lookup:
#for word in listOfStringsThatMightBeWords:
#	if word in wordsDictionary:
#		wordsFound.append(word)
		
# even faster lookup
wordsDictionary = read_english_dictionary.load_words()
# print(wordsDictionary["test"])
for word in listOfStringsThatMightBeWords:
	if word in wordsDictionary.keys():
		wordsFound.append(word)

print("" + str(len(wordsFound)) +  " words found:")
print(wordsFound)

# write to file:
f=open('output.txt','w')
for word in wordsFound:
    f.write(word+'\n')
f.close()

# sort by length:
wordsFoundByLength= wordsFound
wordsFoundByLength.sort(key=len)
longestWord = wordsFoundByLength[len(wordsFoundByLength)-1]
print("words found, sorted by length. Longest = " + longestWord + ", with " + str(len(longestWord)) + " letters")

print("list of words by length:")
print(wordsFoundByLength)

# write to file:
f=open('output_by_length.txt','w')
for word in wordsFoundByLength:
    f.write(word+'\n')
f.close()

print("Wrote the words to file 'output.txt', 'output_by_length.txt'")