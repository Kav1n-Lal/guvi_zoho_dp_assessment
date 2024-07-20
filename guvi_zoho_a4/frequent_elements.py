# Question 4: Top K Frequent Elements
# Given an integer array nums and an integer k, return the k most frequent elements. You may return the
# answer in any order.

# Example:
# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]

def frequent_elements(nums,k):
  for i in nums:
    c[i]=0
  for j in nums:
    c[j]+=1
  p=(list(c.items()))
  z=sorted(p,key=lambda x:x[1],reverse=True)
  z1=[]
  try:
    for b in range(k):
      z1.append(z[b][0])
  except:
    pass
  return (z1)

a1=input().split()
a=list(map(int,a1))
b=int(input())
c={}
frequent_elements(a,b)