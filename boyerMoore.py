# -*-coding=utf-8 -*-
import sys
#sys.setdefaultencoding('utf-8')

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

#print("tes")
s = "Mantab Xiaomi Semoga dedek Xiaomi Fradella Naufalyn sehat dan sukses selalu. 😘😘 https://t.co/RH8n31xzbI"
s.encode('utf-8')
print(bmMatch(s, "Yuk"))