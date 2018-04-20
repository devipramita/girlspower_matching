#-*- coding: utf-8 -*-
import sys, json, re
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
			if (ord(text[i]) != None or ord(text[i]) < 128):
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

def regex_search(pattern, sentence):
    pat = '\w+' + pattern + '\w+'
    match = re.search(pattern, sentence, re.IGNORECASE)
    if match:
        #print('found', pattern)
        return 0
    else:
    	return -1

def regex_findall(sentence, pattern):
    match = re.findall(pattern, sentence)
    count = 0
    for mat in match:
        count += 1
        print('find all',pattern)
    print(count)

def main():
	# Load the data that PHP sent us
	print(sys.argv[2])
	print(sys.argv[3])
	string = sys.argv[1]
	#data = string.split('$')
	#print(data)
	
	string = sys.argv[1]
	pattern = sys.argv[2]
	method = sys.argv[3]
	data = string.split('$')
	#print(data)
	if (method == "kmp"):
		for item in data:
			result = KMPmatch(item,pattern)
			if (result != -1):
				print("SPAM")
			print('1', item)
	print(data)
	if (method == "bm"):
		for x in data:
			print(x)
			result = bmMatch(x,pattern)
			print(result)
			if (result != -1):
				print("SPAM")
			print('1')
	#print(data)
	if (method == "regex"):
		for item in data:
			result = regex_search(pattern,item)
			if (result != -1):
				print("SPAM")
			print(item)
	

if __name__ == '__main__': main()