# 1. Remove Nth Node From End of List
# Problem Statement:
# Given the head of a linked list, remove the nth node from the end of the list and return its head.
# Input Description:
# - head: The head of a singly linked list.
# - n: An integer representing the position from the end of the list.
# Output Description:
# - The head of the modified linked list.
# Constraints:
# - The number of nodes in the list is sz.
# - 1 <= sz <= 30
# - 0 <= Node.val <= 100
# - 1 <= n <= sz
# Example 1:
# Input: head = [1,2,3,4,5], n = 2
# Output: [1,2,3,5]
# Explanation: The second node from the end is 4, so we remove it.
# Example 2:
# Input: head = [1], n = 1
# Output: []
# Explanation: The first node from the end is 1, so we remove it.


#SOLUTION
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length=1

    def __str__(self) -> str:
        nodes = []
        thead = self.head

        while thead != None:
            nodes.append(thead.value)
            thead = thead.next

        #reversing the node list
        return str(nodes)

    def insertAtTail(self, data):
        # create a new node
        newNode = Node(data)

        # check if the list is empty
        if self.head == None:
            # list is empty
            self.head = newNode
        else:
            # list is not empty and has elements
            # create a duplicate pointer
            thead = self.head

            # move the pointer to the tail node
            while thead.next != None:
                thead = thead.next

            # now the thead pointer points to the tail node
            # update the next of the tail node to the newNode
            thead.next = newNode
            self.tail=newNode
            self.length+=1

    def pop(self,index):
      if index<0 or index>=self.length:
        return None
      elif index==0:
        thead=self.head
        self.head=self.head.next
        thead.next=None
        self.length-=1
        return True
      else:
        pre=self.head
        thead=self.head
        for _ in range(index):
          pre=thead
          thead=thead.next
        pre.next=thead.next
        thead.next=None
      self.length-=1
      return True



a=input().split()
b=int(input())
c=len(a)-b

list_ = LinkedList()
for i in a:
  list_.insertAtTail(i)

list_.pop(c)

print(list_)