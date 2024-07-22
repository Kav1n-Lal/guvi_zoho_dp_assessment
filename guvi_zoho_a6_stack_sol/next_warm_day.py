# 3. Daily Temperatures
# Problem Description:
# Given a list of daily temperatures T, return a list such that, for each day in the input, tells you how many days you would
# have to wait until a warmer temperature. If there is no future day for which this is possible, put 0 instead.
# Input:
# - An array of integers T representing the daily temperatures.
# Output:
# - Return an array of integers, where the ith element is the number of days you have to wait until a warmer temperature.
# If there is no future day for which this is possible, put 0 instead.
# Example 1:
# Input: [73, 74, 75, 71, 69, 72, 76, 73]
# Output: [1, 1, 4, 2, 1, 1, 0, 0]
# Constraints:
# - 1 <= T.length <= 10^5
# - 30 <= T[i] <= 100

#SOLUTION
class Stack:
    def __init__(self):
        self.items = []
        self.top = -1

    def push(self, data):
        self.items.append(data)
        self.top += 1

    def next_warm_day(self):
      s=[]
      try:
        
        i=0
        while len(self.items)!=0:
          j=0
          while j<self.top:
            if self.items[0]<self.items[j]:
              s.append(j)
              self.items.pop(0)
              j=0
            elif self.items[0]>max(self.items[j:]):
              s.append(0)
              self.items.pop(0)
              j=0
            j+=1
          i=0
      except IndexError:
        s.append(0)
      
      return s

# testing the stack class

temp1 = input().split()
temp=list(map(int,temp1))

stack = Stack()
for t in temp:
  stack.push(t)

print(stack.items)
print(stack.next_warm_day())