# A sample Tkinter program for passwords

from tkinter import *
from tkinter import ttk
root = Tk()

box = ttk.Entry(root,show = "•")
box.pack()

def show():
    global box, check
    if checked.get():
        box.config(show="")
    else:
        box.config(show="•")
checked=IntVar()
check = ttk.Checkbutton(root,text="Show password?",command=show,variable=checked)
check.pack()

root.mainloop()
