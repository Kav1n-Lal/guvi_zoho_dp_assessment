# Question 3: Longest Substring Without Repeating Characters
# Given a string s, find the length of the longest substring without repeating characters.

# Example:
# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.

def longest_substring(e):
  s=list(e)
  #print(s)
  f=[]
  for i in range(len(s)):
    if s[i] not in f:
      f.append(s[i])
      s[i]=''
    else:
      d.append(''.join(f))
      f.clear()
      y=(''.join(s))
      longest_substring(y)
  
  d.append(''.join(f))
  f.clear()
  y=(''.join(s))
  

d=[]
a1=input()
longest_substring(a1)
v=sorted(d,key=len,reverse=True)
#print(v)
print(len(v[0]))
  