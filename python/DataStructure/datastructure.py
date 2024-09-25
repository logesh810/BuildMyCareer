import DataStructure.linkedlist as ll
import DataStructure.stack as st

def Info():
    print("*****************")
    print("1. Array")
    print("2. LinkedList")
    print("3. Stack")
    defineAction()


def defineAction():
    userInput = input("Give the input: ")
    if userInput=="1":
        Array()
    elif userInput=="2":
        LinkedList()
    elif userInput=="3":
        StackFunction()
    else:
        print("Invalid input")
        
        
def Array():
    print("Array def")
def LinkedList():
   ll.Info()
def StackFunction():
    st.Info()