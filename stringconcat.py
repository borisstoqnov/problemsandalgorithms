##print a string to a certain character and include only unique values:
def merge_the_tools(string, k):
	n = len(string)
	t = n/int(k)
	temp = []
	counter = 0
	for i in string:
		counter += 1
		if i not in temp:
			temp.append(i)
		if counter == k:
			print("".join(temp))
			temp = []
			counter = 0