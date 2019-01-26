from index import *
from tkinter import *
from functools import partial
top = Tk()

"""
f = Frame(height=50, width=200)
f.pack_propagate(0) # don't shrink
f.pack()
"""

top.title("PROJECT")
bt = [None for i in range(1, 20)]
mlb = Label(top, text = "VERSION CONTROL", bg = "orange",  fg = "pink")
mlb.config(font=("Courier", 44))
mlb.pack()
lb = Label(top, text = "MENU", fg = "dark blue")
lb.config(font=("Helvetica 16 bold italic", 30))
lb.pack()
bt[1] = "List Files" 
bt[2] = "View File"
bt[3] = "New File"
bt[4] = "Delete File"
bt[5] = "Edit File"
bt[6] = "List Branches"
bt[7] = "New Branch"
bt[8] = "Switch Branch"
bt[9] = "Exit"

for i in range(1, 10):
	bt[i] = Button(top, text = bt[i], command = partial(callMenu, i), borderwidth = 3, height = 2, activebackground = "green")

for i in range(1, 10):
	bt[i].pack()

lb1 = Label(top, text = "MADE BY\n", fg = "purple", bg = "pink")
lb1.config(font = ("Roman", 22))
lb1.pack()
lb2 = Label(top, text = "Yogesh Choubey : 17IT252\n", font = "Roman", fg = "dark blue")
lb2.pack()
lb3 = Label(top, text = "Dhruvik : 17IT225\n", font = "Roman", fg = "dark blue")
lb3.pack()
lb4 = Label(top, text = "Rakesh Pavan : 17IT154\n", font = "Roman", fg = "dark blue")
lb4.pack()
lb5 = Label(top, text = "Neeraj : 17IT226", font = "Roman", fg = "dark blue")
lb5.pack()


top.mainloop()


#tkinter.Button(top, text =2, command = partial(initialize, "2"))