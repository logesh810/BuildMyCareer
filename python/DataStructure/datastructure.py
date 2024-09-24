import DataStructure.linkedlist as ll

def Info():
    print("*****************")
    print("1. Array")
    print("2. LinkedList")
    defineAction()


def defineAction():
    userInput = input("Give the input: ")
    if userInput=="1":
        Array()
    elif userInput=="2":
        LinkedList()
    else:
        print("Invalid input")
        
        
def Array():
    print("Array def")
def LinkedList():
   ll.Info()