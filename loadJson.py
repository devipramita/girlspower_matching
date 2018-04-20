import sys, json

# KMP

# string S
# size m
# any index k
# j mismatch position
# k = j-1
def suffix(string):
	suff = []
	a = ""
	for x in range(1,len(string)):
		a = string + x
		suff += a

def prefix(string):
	pref = []
	a = ""
	for x in range(0,len(string)):
		a += string[x]
		pref += a

def border(k, string):
	proc = string[0:k]
	s = suffix(proc)
	p = prefix(proc)
	max = 0
	for a in s:
		if (a in p) and (len(a) > max):
			max = len(a)
	return max

def KMPmatch(text, pattern):
	n = len(text)
	m = len(pattern)
	fail = computeFail(pattern)
	i = 0
	j = 0
	while (i < n):
		if (pattern[j] == text[i]):
			if (j == m - 1):
				return i - m + 1 #match
			i+=1
			j+=1
		elif (j > 0):
			j = fail[j-1]
		else:
			i+=1
	return -1; 

def computeFail(pattern):
	fail = [0] *10000
	m = len(pattern)
	j = 0
	i = 1
	while (i < m):
		if (pattern[j] == pattern[i]):#j+1 chars match
			fail[i] += j + 1
			i+=1
			j+=1
		elif (j > 0): # j follows matching prefix
			j = fail[j-1]
		else: #no match
			fail[i] = 0
			i+=1
	return fail

def main():
	# Load the data that PHP sent us
	print(sys.argv[2])
	print(sys.argv[3])
	string = sys.argv[1]
	data = string.split('$')
	#print(data)
	print(data)

	

if __name__ == '__main__': main()