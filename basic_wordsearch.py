# Importing the wordsearch (assume it's a rectangle!)

# do the imports
import sys # for file access
import my_split # for splitting strings by multiple delimiters

# my_split notes:
# print(my_split.my_split('1111  2222 3333;4444,5555;6666', [' ', ';', ',']))

# specify wordsearch file:
wordsearch_file= 'wordsearch_test_1.txt'

# specify delimiters
multipleDelimiters= [' ', ';', ',', '.', '-', '=', '<', '>', '*', '/', '\\', '_', '[', ']']

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

for iRow in range(1,nLines):
	print(str(iRow) + " = " + strWordsearch[iRow])
#	for iCol in range(1,nRows):
#		print("row=" + str(iRow) + " col=" + str(iCol) + ". Char=" + strWordsearch[iRow][iCol])

# try and build a list of ascii characters:
print(my_split.my_split('1111  2222 3333;.4444,5555;6666', multipleDelimiters))
print(my_split.my_split('.....G...', multipleDelimiters))

for iRow in range(1,nLines):
	print(str(iRow) + " = " + "%s",my_split.my_split(strWordsearch[iRow],multipleDelimiters))

