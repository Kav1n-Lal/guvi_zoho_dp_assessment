# Question 1: Two Sum
# Given an array of integers nums and an integer target, return indices of the two numbers such that they
# add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same
# element twice.
# You can return the answer in any order.

# Example:
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

def return_indices(num_list,target):
  s=[]
  i=0
  while True:
    t=target-num_list[i]
    if t in num_list:
      s.append(num_list.index(num_list[i]))
      s.append(num_list.index(t,i+1))
    i+=1
    return s
a1=input().split()
a=list(map(int,a1))
b=int(input())
return_indices(a, b)
