# Question 5: Valid Anagram
# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

# Example:
# Input: s = "anagram", t = "nagaram"
# Output: true

# Input: s = "rat", t = "car"
# Output: false

def anagram(a,b):
  for i in a:
    c[i]=0
  for j in a:
    c[j]+=1
  q=list(c.items())
  q=sorted(q,key=lambda x:x[0])
  #print(q)
  
  for i1 in b:
    d[i1]=0
  for j1 in b:
    d[j1]+=1
  q1=list(d.items())
  q1=sorted(q1,key=lambda x:x[0])
  #print(q1)

  if q==q1:
    print('true')
  else:
    print('false')



a=list(input())
b=list(input())
c={}
d={}
anagram(a,b)