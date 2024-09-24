import utils as u


class SllNode:
    def __init__(self,data=None) -> None:
        self.data = data
        self.next = None



class Sll:
    def __init__(self) -> None:
        self.head = None
        
    def insertAtBeginning(self,data):
        newNode = SllNode(data)
        newNode.next = self.head
        self.head = newNode
        
        
    def insertAtEnd(self,data):
        newNode = SllNode(data)
        if self.head == None:
            self.head = newNode
            return
        lastNode = self.head
        while lastNode.next:
            lastNode = lastNode.next
        lastNode.next = newNode
        
    def printSll(self):
        tempNode = self.head
        while tempNode:
            print(tempNode.data,end=' ')
            tempNode = tempNode.next
        print()
            
            
def SinglyLinkedList():
    sll =  Sll()
    sll.insertAtBeginning(5)
    sll.insertAtEnd(2)
    sll.insertAtBeginning(500)
    sll.insertAtBeginning(777)
    sll.insertAtEnd(777)
    sll.printSll()
                
def Info():
    print("*****************")
    print("1. Singly Linked List")
    print("2. Doubly Linked List")
    defineAction()

def defineAction():
    userInput = input("Give the input: ")
    if userInput=="1":
        u.clear()
        SinglyLinkedList()
    elif userInput=="2":
        pass
    else:
        print("Invalid input")
    
    