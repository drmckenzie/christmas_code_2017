# this should produce a list of strings from a string array

if __name__ == '__main__':
	# scraping the input
	generate_diagonal_list(t)

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
	maxRow= 4
	maxCol= 4
	
	noIterations = maxRow + maxCol - 1
	
	thisIter= 0
	thisRow= 0
	thisCol= 0
	while thisIter < noIterations:
		if (thisRow<maxRow):
			thisRow= thisIter
		else:
			thisRow= maxRow

		print("iter="+str(thisIter))
		print("row ="+str(thisRow))
		print("col ="+str(thisCol))
		
		thisCol= 0
		while (thisRow>-1) and (thisCol>-1) and (thisCol<maxCol):
			if (thisRow>=maxRow):
				thisRow= maxRow-1
				thisCol= thisIter -maxCol+1

			print("R" + str(thisRow) + " C" + str(thisCol) )
			thisRow= thisRow - 1
			thisCol= thisCol + 1

			
		thisIter += 1
		

		