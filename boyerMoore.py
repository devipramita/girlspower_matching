# -*- coding: utf-8 -*-

def bmMatch(text, pattern):
	#btw last occurence di slide buat apa si wkwk
	last = buildLast(pattern)
	n = len(text)
	m = len(pattern)
	i = m-1
	if (i > n-1):
		return -1
	j = m-1
	status = True
	while status:
		if (pattern[j] == text[i]):
			if (j==0):
				return i
			else: #looking-glass technique
				i = i-1
				j = j-1
		else: #character jump technique
			if (ord(text[i]) != None):
				lo = last[ord(text[i])]
			else:
				lo = -1
			i = i+m-min(j, 1+lo)
			j = m-1
		if (i > n-1):
			status = False
	return -1

def buildLast(pattern):
	last = list()
	for i in range (0, 257):
		last.append(-1)
	for i in range (0, len(pattern)):
		last[ord(pattern[i])] = i

	return last