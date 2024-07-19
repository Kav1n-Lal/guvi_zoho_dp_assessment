# Question 2

# Problem Description:
# Given a string `s`, return the longest palindromic substring in `s`.

# Input Description:
# A string `s`.

# Output Description:
# The longest palindromic substring in `s`.

# Examples:
# **Example 1:**
# - Input: `s = "babad"`
# - Output: `"bab"`
# - Explanation: `"aba"` is also a valid answer.

# **Example 2:**
# - Input: `s = "cbbd"`
# - Output: `"bb"`

# Constraints:
# 1 <= s.length <= 1000
# s consists of only digits and English letters.

#SOLUTION
a=input()
s=[]
for i in range(len(a)):
  for j in range(len(a),0,-1):
    if a[i:j]==a[i:j][::-1]:
      s.append(a[i:j])
      if s[-1]=='':
        break
s1=sorted(s,key=len,reverse=True)       
print(s1[0])
