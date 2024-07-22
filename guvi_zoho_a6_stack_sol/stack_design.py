# Problem Description:
# Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
# Implement the MinStack class:
# - MinStack(): initializes the stack object.
# - void push(int val): pushes the element val onto the stack.
# - void pop(): removes the element on the top of the stack.
# - int top(): gets the top element of the stack.
# - int getMin(): retrieves the minimum element in the stack.
# Example 1:
# MinStack minStack = new MinStack();
# minStack.push(-2);
# minStack.push(0);
# minStack.push(-3);
# minStack.getMin(); // return -3
# minStack.pop();
# minStack.top(); // return 0
# minStack.getMin(); // return -2
# Constraints:
# - -2^31 <= val <= 2^31 - 1
# - Methods pop(), top(), and getMin() operations will always be called on non-empty stacks.
# - At most 3 * 10^4 calls will be made to push, pop, top, and getMin

#SOLUTION
class Stack:
    def __init__(self):
        self.items = []
        self.top = -1

    def push(self, data):
        self.items.append(data)
        self.top += 1

    def pop(self):
        self.items.pop()
        self.top -= 1

    def isEmpty(self):
        return self.top == -1

    def top_peek(self):
        return self.items[-1]
    
    def getMin(self):
      a=min(self.items)
      b=self.items.index(a)
      return a




obj=input().split()
obj=[int(i) for i in obj]

# testing the stack class
stack = Stack()
for i in obj:
  stack.push(i)

# print(stack.items)
# print(stack.getMin())
# stack.pop()
# print(stack.top_peek())
# print(stack.getMin())
# print(stack.items)
