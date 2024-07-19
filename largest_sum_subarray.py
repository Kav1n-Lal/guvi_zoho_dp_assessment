# Question 4

# Problem Description:
# Given an integer array `nums`, find the subarray with the largest sum, and return its sum.

# Input Description:
# An integer array `nums`.

# Output Description:
# The sum of the subarray with the largest sum.

# Examples:
# **Example 1:**
# - Input: `nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]`

# - Output: `6`
# - Explanation: The subarray `[4, -1, 2, 1]` has the largest sum `6`.

# **Example 2:**
# - Input: `nums = [1]`
# - Output: `1`
# - Explanation: The subarray `[1]` has the largest sum `1`.

# **Example 3:**
# - Input: `nums = [5, 4, -1, 7, 8]`
# - Output: `23`
# - Explanation: The subarray `[5, 4, -1, 7, 8]` has the largest sum `23`.

# Constraints:
# 1 <= nums.length <= 10^5
# -10^4 <= nums[i] <= 10^4


#SOLUTION
def largest_subarray_sum(num_list):

  largest_sum=0
  i=0
  while i<len(num_list):
    arr_sum=sum(num_list[i:])
    if arr_sum>largest_sum:
      largest_sum=arr_sum
    i+=1

  for j in range(len(num_list)):
    for k in range(len(num_list),0,-1):
      d=sum(num_list[j:k])
      if d>largest_sum:
        largest_sum=d
      k-=1
    j+=1
  return largest_sum


f=input().split()
x=list(map(int,f))
largest_subarray_sum(x)