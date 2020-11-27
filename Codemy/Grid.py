from tkinter import *

root = Tk()

#Creating a Label Widget
myLabel1 = label(root, text = "Hello World!").grid(row=0, column=0)
myLabel2 = label(root, text = "Hello World!").grid(row=1, column=1)

#Showing it onto the screen
myLabel1.pack()
myLabel2.pack()

root.mainloop()
