# Importing the wordsearch (assume it's a rectangle!)

# do the imports
import sys # for file access

# specify wordsearch file:
wordsearch_file= 'wordsearch_test_1.txt'

f = open(wordsearch_file,'r')
nLines= 0
nRows= 0
strWordsearch= []
for line in iter(f):
	strWordsearch.append(line.rstrip())
	nLines += 1
	if ( nRows == 0 ):
		nRows= len(line.rstrip())
	else:
		if ( nRows != len(line.rstrip()) ):
			print("something strange went on here.")
			
f.close()

print(strWordsearch[0])
print(strWordsearch[5])
print("No. Lines = " + str(nLines))
print("No. rows = " + str(nRows))

