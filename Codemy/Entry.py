from tkinter import *

root = Tk()

def onClick():
    Label(root, text="Hello "+e.get()).pack()

e1 = Entry(root)
e2 = Entry(root,width=50)
e3 = Entry(root,width=50,borderwidth=5)
e4 = Entry(root,width=50,bg="#0d0da1",fg="white")
e = Entry(root,width=50)
e.insert(0,"Enter your name")

e1.pack()
e2.pack()
e3.pack()
e4.pack()
e.pack()

Button(root,text="Submit",command=onClick).pack()

root.mainloop()
