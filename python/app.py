import DataStructure.datastructure as ds
import utils as u

def Info():
     print("*****************")
     print("1. Data Structure")
     print("2. Exit")
     print("3. Clear")
     defineAction()


def defineAction():
    userInput = input("Give the input: ")
    if userInput=="1":
        u.clear()
        ds.Info()
    elif userInput=="2":
        exit()
    elif userInput=="3":
        u.clear()
    else:
        print("Invalid input")

Info()



