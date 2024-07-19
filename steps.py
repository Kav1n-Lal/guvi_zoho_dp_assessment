# Question 5

# Problem Description:
# You are climbing a staircase. It takes `n` steps to reach the top.

# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

# Input Description:
# An integer `n`.

# Output Description:

# The number of distinct ways to climb to the top.

# Examples:
# **Example 1:**
# - Input: `n = 2`
# - Output: `2`
# - Explanation: There are two ways to climb to the top.
# 1. 1 step + 1 step
# 2. 2 steps

# **Example 2:**
# - Input: `n = 3`
# - Output: `3`
# - Explanation: There are three ways to climb to the top.
# 1. 1 step + 1 step + 1 step
# 2. 1 step + 2 steps
# 3. 2 steps + 1 step

# Constraints:
# 1 <= n <= 45


#SOLUTION
o=[]
def main(a):
  s1=[1 for j in range(a)]
  o.append(s1)
  s=[1,2]
  h=[]
  
  def no_of_steps():
    i=0
    while i<len(s):
      h.append(s[i])
      i+=1
    if sum(h)<a:
      no_of_steps()
    elif sum(h)>a:
      h.pop(-1)
      if sum(h)!=a:
        h.append(2)
        h.pop(-2)
  
  no_of_steps()

  def permute(m,k,l):
    if k==l:
      o.append(list(m))
    else:
      for g in range(k,l):
        m[k],m[g]=m[g],m[k]
        permute(m,k+1,l)
        m[g],m[k]=m[k],m[g]
  
  #finding all the possible combinations
  permute(h,0,len(h))
  #return h

a=int(input())
main(a)
o1=[]
for p in o:
  if p not in o1:
    o1.append(p)
print(f"Different steps combinations: {o1}")
print(f"total combinations count: {len(o1)}")
