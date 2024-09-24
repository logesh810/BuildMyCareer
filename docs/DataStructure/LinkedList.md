# [Day 2: Linked Lists](https://docs.google.com/spreadsheets/d/1pViJo3jAgve8OB_qHbircFv4lW214_9edoSmc5Yq6RA/edit?gid=0#gid=0?target=_blank)

* Concepts to Learn: Singly linked lists, doubly linked lists.
* Topics:
    * Creating and traversing linked lists.
    * Insertion and deletion of nodes.
    * Reversing a linked list
* Practice Problems:
    * Implement a singly linked list from scratch.
    * Detect a cycle in a linked list.
    * Merge two sorted linked lists.
* Resources:
    * Linked List in C# (GeeksforGeeks)
    * [LeetCode Problem Set: Linked List](https://leetcode.com/problem-list/linked-list/)


## Types of Linked Lists
* Singly linked lists
* Doubly linked lists
* Circular linked lists
    * Circular singly linked list
    * Circular doubly linked list

### Singly linked Lists
A singly linked list is the simplest kind of linked lists. It takes up less space in memory because each node has only one address to the next node, like in the image below.

![alt text](https://www.w3schools.com/dsa/img_linkedlists_singly.svg)

```
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
node1 = Node(3)
node2 = Node(5)
node3 = Node(13)
node4 = Node(2)

node1.next = node2
node2.next = node3
node3.next = node4

currentNode = node1
while currentNode:
    print(currentNode.data, end=" -> ")
    currentNode = currentNode.next
print("null")

```

### Doubly linked Lists
A doubly linked list has nodes with addresses to both the previous and the next node, like in the image below, and therefore takes up more memory. But doubly linked lists are good if you want to be able to move both up and down in the list.

![alt text](https://www.w3schools.com/dsa/img_linkedlists_doubly.svg)

```

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
    
node1 = Node(3)
node2 = Node(5)
node3 = Node(13)
node4 = Node(2)

node1.next = node2

node2.prev = node1
node2.next = node3

node3.prev = node2
node3.next = node4

node4.prev = node3

print("\nTraversing forward:")
currentNode = node1
while currentNode:
    print(currentNode.data, end=" -> ")
    currentNode = currentNode.next
print("null")

print("\nTraversing backward:")
currentNode = node4
while currentNode:
    print(currentNode.data, end=" -> ")
    currentNode = currentNode.prev
print("null")

```

### circular linked Lists
A circular linked list is like a singly or doubly linked list with the first node, the "head", and the last node, the "tail", connected.

In singly or doubly linked lists, we can find the start and end of a list by just checking if the links are null. But for circular linked lists, more complex code is needed to explicitly check for start and end nodes in certain applications.

Circular linked lists are good for lists you need to cycle through continuously.

The image below is an example of a singly circular linked list:
![altext](https://www.w3schools.com/dsa/img_linkedlists_circsingly.svg)

The image below is an example of a doubly circular linked list:

![altext](https://www.w3schools.com/dsa/img_linkedlists_circdoubly.svg)