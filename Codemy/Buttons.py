from tkinter import *

root = Tk()

def myclick():
    Label(root, text="I clicked a button!").pack()

myButton1 = Button(root, text="Click Me!", command=myclick)
#DISABLED Button
myButton2 = Button(root, text="Click Me!", state=DISABLED)
myButton3 = Button(root, text="Click Me!", padx=50)
myButton4 = Button(root, text="Click Me!", pady=50)
myButton5 = Button(root, text="Click Me!", padx=50, pady=50)
#You can also use hexcode in bg and fg
myButton6 = Button(root, text="Click Me!", fg="white", bg="black")

myButton1.pack()
myButton2.pack()
myButton3.pack()
myButton4.pack()
myButton5.pack()
myButton6.pack()

root.mainloop()
