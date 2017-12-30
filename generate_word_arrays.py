# automating the chore of generating the word arrays.
# for example if we have an array of [abcd], we want returned:
# [a,b,c,d,ab,bc,cd,abc,bcd,abcd]

# seems this has been solved:
# https://codegolf.stackexchange.com/a/83746

if __name__ == '__main__':
	# scraping the input
	generate_word_arrays(t)

def generate_word_arrays(t):
	l= len(t)
	# iterator
	n= 0
	# the output:
	strOutput= []
	for j in range(l):
		for i in range(l):
			if i>=j:
				print(j*' '+t[j:i+1])
				strOutput.append(t[j:i+1])
	#
	# now make sure it's unique:
	strOutputUnique = list(set(strOutput))
	print("Unique list, unsorted")
	print(strOutputUnique)
	strOutputUnique.sort()
	print("Unique list, sorted")
	print(strOutputUnique)
	
	return strOutputUnique