from PersistentBST2 import *
from tkinter import messagebox as tkMessageBox
import sys

Tree = PBST()
currentBranch = "master"
prevBranch = None
branches = ["master"]
def callMenu(choice):

    global currentBranch
    global prevBranch
    global branches
   
    if choice == 1:
        res = Tree.inFix(currentBranch)
        temp=""
        temp += "Branch:" + currentBranch
        temp += "\nFiles:\n\n"
        if res == None:
            tkMessageBox.showinfo("Result", "File list is empty!!!")
        else:
            for i in res:
                temp = temp + i
                temp = temp +"\n"
            tkMessageBox.showinfo("Result", temp)

    elif choice == 2:
        name = input("Enter name of file to be opened: ")
        file = Tree.search(name, currentBranch)
        if file is None:
            tkMessageBox.showinfo("Result", "File does not exist!")
        else:
            res = file.getData()
            temp = ""
            temp += "Branch:" + currentBranch
            temp +="\n"
            temp += res
            tkMessageBox.showinfo("Result", temp)

    elif choice == 3:
        name = input("Enter name of new file: ")
        Tree.insert(name, currentBranch)

    elif choice == 4:
        name = input("Enter name of file to be deleted: ")
        Tree.delete(name, currentBranch)

    elif choice == 5:
        name = input("Enter name of file to be edited: ")
        Tree.edit(name, currentBranch)

    elif choice == 6:
        temp = "Branches:\n"

        for branch in branches:
            temp += branch + "\n"
        tkMessageBox.showinfo("Result", temp)

    elif choice == 7:
        branchName = input("Enter name of new branch: ")
        if branchName in branches:
            temp = currentBranch + "\n"
            tkMessageBox.showinfo("Result", temp + "Branch already exist!!!")
        else:
            prevBranch, currentBranch = currentBranch, branchName
            temp = Tree.newBranch(currentBranch, prevBranch)
            if temp == False:
                tkMessageBox.showinfo("Result", "Invalid:Current Branch is empty!!!")
                currentBranch = prevBranch
            else:    
                branches.append(branchName)
           

    elif choice == 8:
        branchName = input("Enter name of branch to switch to: ")
        if branchName not in branches:
            temp = "Branch:" + currentBranch + "\n"
            temp += branchName +" "
            tkMessageBox.showinfo("Result", temp + "branch does not exist!!!")   
        else:
            prevBranch, currentBranch = currentBranch, branchName
            temp = "Branch changed to " + currentBranch
            tkMessageBox.showinfo("Result", temp)
    elif choice == 9:
        sys.exit("Exiting the program...")


