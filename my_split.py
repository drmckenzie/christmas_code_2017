# from https://stackoverflow.com/a/2911664/1530103

if __name__ == '__main__':
	my_split(s, seps)

def my_split(s, seps):
	res = [s]
	for sep in seps:
		s, res = res, []
		for seq in s:
			res += seq.split(sep)
	# filter the list for zero lengths:
	res = [x for x in res if x]
	return res
