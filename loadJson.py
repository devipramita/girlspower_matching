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
 alphabet = set(text)
 last = buildLast(pattern, alphabet)
 n = len(text)
 m = len(pattern)
 i = m-1
 if (i < n):
  status = True
 else:
  status = False
 j = m-1
 while status:
  if (pattern[j] == text[i]):
   if (j==0):
    return i
   else: #looking-glass technique
    i = i-1
    j = j-1
  else: #character jump technique
   #print("hehee", text[i])
   lo = last(text[i])
   i = i+m-min(j, 1+lo)
   j = m-1
  if (i >= n):
   status = False
 return -1

class buildLast(object):

 def __init__(self, pattern, alphabet):
  self.occurrences = dict()
  for letter in alphabet:
   self.occurrences[letter] = pattern.rfind(letter)

 def __call__(self, letter):
  return self.occurrences[letter]

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
	#print(sys.argv[2])
	#print(sys.argv[3])
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
				print("!!!SPAM!!!")
			print(item)
			print("SPLIT")
	#print(data)
	if (method == "bm"):
		for x in data:
			result = bmMatch(x,pattern)
			if (result != -1):
				print("!!!SPAM!!!")
			print(x)
			print("SPLIT")
	#print(data)
	if (method == "regex"):
		for item in data:
			result = regex_search(pattern,item)
			if (result != -1):
				print("!!!SPAM!!!")
			print(item)
			print("SPLIT")
	

if __name__ == '__main__': main()