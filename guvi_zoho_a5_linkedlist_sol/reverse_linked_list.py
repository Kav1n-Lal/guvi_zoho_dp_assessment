# 2. Reverse Linked List
# Problem Statement:
# Reverse a singly linked list.
# Input Description:
# - head: The head of a singly linked list.
# Output Description:
# - The head of the reversed linked list.
# Constraints:
# - The number of nodes in the list is sz.
# - 1 <= sz <= 5000
# - -5000 <= Node.val <= 5000
# Example 1:
# Input: head = [1,2,3,4,5]
# Output: [5,4,3,2,1]
# Example 2:
# Input: head = [1,2]
# Output: [2,1]

#SOLUTION
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.length=1

    def __str__(self) -> str:
        nodes = []
        thead = self.head

        while thead != None:
            nodes.append(thead.value)
            thead = thead.next

        #reversing the node list
        return str(nodes[::-1])

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
            self.length+=1



reverse_list = LinkedList()

a=input().split()
for i in a:
  reverse_list.insertAtTail(i)

print(reverse_list)
