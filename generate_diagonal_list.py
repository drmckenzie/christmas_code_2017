# this should produce a list of strings from a string array

if __name__ == '__main__':
	# scraping the input
	generate_diagonal_list(t)
	print("This appears to work for the square case.")
	print("You know, this could just be hacked so that the rectangular matrix is padded with whitespace, then trimmed at the end...")

def generate_diagonal_list(t):
	# start from 1,1 and iterate until we have max row or max col
	# so, for a 4row x 8col, we should have:
	# 1,1
	# 1,2 2,1
	# 1,3 2,2 3,1
	# 1,4 2,3 3,2 4,1
	# 2,5 3,4 4,3
	# 3,6 4,7
	# 4,8
	
	# get max row & col lengths:
	maxRow= len(t)
	maxCol= len(t[0])
	#print("maxRow ="+str(maxRow))
	#print("maxCol ="+str(maxCol)) 
	
	# make it square 
	# NOTE: this is a bodge. Mainly because it doesn't work in rectangular mode yet. There's a row that gets counted twice, and I can't figure out where in the code it is. 
	#todo 
	maxBoth= max(maxRow,maxCol)
	for iRow in range(0,maxBoth):
		#print(t[iRow])
		if iRow>(maxRow-1):
			t.append(maxBoth*' ')
			#print("row appended")
		for iCol in range(0,maxBoth):
			if iCol>(maxCol-1):
				#print("col appended")
				tempString = t[iRow] + " "
				t[iRow]= tempString
				#print(t[iRow][iCol])

	#for iRow in range(0,maxBoth):
	#	print("."+t[iRow]+".")
				
	# get new maximums
	maxRow= len(t)
	maxCol= len(t[0])
	#print("maxRow ="+str(maxRow))
	#print("maxCol ="+str(maxCol)) 
	
	# number of iterations
	noIterations = maxRow + maxCol - 1
	
	thisIter= 0
	thisRow= 0
	thisCol= 0
	allDiagStrings= []
	while thisIter < noIterations:
		if (thisRow<maxRow):
			thisRow= thisIter
		else:
			thisRow= maxRow

		#print("iter="+str(thisIter))
		#print("row ="+str(thisRow))
		#print("col ="+str(thisCol))
		
		thisCol= 0
		thisDiagonalString= []
		while (thisRow>-1) and (thisCol>-1) and (thisCol<maxCol):
			if (thisRow>=maxRow):
				thisRow= maxRow-1
				thisCol= thisIter -maxCol+1

			#print("R" + str(thisRow) + " C" + str(thisCol) )
			thisDiagonalString.append(t[thisRow][thisCol])
			
			thisRow= thisRow - 1
			thisCol= thisCol + 1
			
		allDiagStrings.append(''.join(thisDiagonalString).strip())
		
		thisIter += 1
	
	# delete the end empty string (if exists)
	while allDiagStrings[len(allDiagStrings)-1]=='':
		allDiagStrings= allDiagStrings[0:(len(allDiagStrings)-1)]
	
	#print(allDiagStrings)
	return allDiagStrings	
	