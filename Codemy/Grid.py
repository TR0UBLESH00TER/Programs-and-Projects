from tkinter import *

root = Tk()

#Creating a Label Widget
Label(root, text = "Hello World!").grid(row=0, column=0)
Label(root, text = "~Tkinter").grid(row=1, column=1)

'''
OR
#Creating a Label Widget
myLabel1 = Label(root, text = "Hello World!")
myLabel2 = (root, text = "~Tkinter")

myLabel2.grid(row=0, column=0)
myLabel2.grid(row=1, column=1)
'''

root.mainloop()
