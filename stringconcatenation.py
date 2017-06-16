import sys
def duplication(x):
	s = "0"
	t = "1"
	tinit = ""
	concat = s + t
	s = concat
	while len(s) < 1000:
		for n in s:
			if n == "0":
				t = "1"
			elif n == "1":
				t = "0"
			tinit += t
		concat = s + tinit
		s = concat
		tinit = ""
	return (s[x])

q = int(input().strip())
for a0 in range(q):
	x = int(input().strip())
	result = duplication(x)
	print(result)
##check if anagram
def checkif_anagram(s1,s2):
	firstlist = list(s1)
	secondlist = list(s2)

	if len(firstlist)==len(secondlist):
		for i in firstlist:
			if i in secondlist:
				secondlist.remove(i)
				firstlist.remove(i)
			else:
				return 1
				print("is not anagram")
	else:
		return 1
	print("is anagram")
checkif_anagram("kuree","rukee")