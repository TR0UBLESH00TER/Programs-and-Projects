from tkinter import *

root=Tk()
root.title("Calculator")
root.configure(bg='Black',padx=10,pady=10)


e=Entry(root, width=88, borderwidth=1, bg = 'Black', fg = 'white')
e.grid(row=0, column=0, columnspan=5, pady=5)

# Functions
def button(n):
    global e
    if e.get() == "ERROR":
        e.delete(0,END)
    e.insert(END,n)

def button_del():
    global e
    if e.get() == "ERROR":
        e.delete(0,END)
    else:
        e.delete(len(e.get())-1)

def button_clr():
    global e
    if e.get() == "ERROR":
        e.delete(0,END)
    e.delete(0,END)

def button_equal():
    global e
    Input = e.get()
    e.delete(0,END)
    try:
        e.insert(END,eval(Input))
    except Exception:
        e.insert(END,"ERROR")

def button_add():
    global e
    if e.get() == "ERROR":
        e.delete(0,END)
    e.insert(END,"+")

def button_minus():
    global e
    if e.get() == "ERROR":
        e.delete(0,END)
    e.insert(END,"-")

def button_into():
    global e
    if e.get() == "ERROR":
        e.delete(0,END)
    e.insert(END,"×")

def button_div():
    global e
    if e.get() == "ERROR":
        e.delete(0,END)
    e.insert(END,"×")


# Buttons
button0=Button(root, text="0", padx=140, borderwidth=3, command=lambda:button(0), activebackground='grey', fg= 'white', bg = 'black', pady=10, font=('Courier', 10))
button1=Button(root, text="1", padx=40, borderwidth=3, command=lambda:button(1), activebackground='grey', fg= 'white', bg = 'black', pady=10, font=('Courier', 10))
button2=Button(root, text="2", padx=40, borderwidth=3, command=lambda:button(2), activebackground='grey', fg= 'white', bg = 'black', pady=10, font=('Courier', 10))
button3=Button(root, text="3", padx=40, borderwidth=3, command=lambda:button(3), activebackground='grey', fg= 'white', bg = 'black', pady=10, font=('Courier', 10))
button4=Button(root, text="4", padx=40, borderwidth=3, command=lambda:button(4), activebackground='grey', fg= 'white', bg = 'black', pady=10, font=('Courier', 10))
button5=Button(root, text="5", padx=40, borderwidth=3, command=lambda:button(5), activebackground='grey', fg= 'white', bg = 'black', pady=10, font=('Courier', 10))
button6=Button(root, text="6", padx=40, borderwidth=3, command=lambda:button(6), activebackground='grey', fg= 'white', bg = 'black', pady=10, font=('Courier', 10))
button7=Button(root, text="7", padx=40, borderwidth=3, command=lambda:button(7), activebackground='grey', fg= 'white', bg = 'black', pady=10, font=('Courier', 10))
button8=Button(root, text="8", padx=40, borderwidth=3, command=lambda:button(8), activebackground='grey', fg= 'white', bg = 'black', pady=10, font=('Courier', 10))
button9=Button(root, text="9", padx=40, borderwidth=3, command=lambda:button(9), activebackground='grey', fg= 'white', bg = 'black', pady=10, font=('Courier', 10))

button_clr=Button(root, text=" C ", padx=40, borderwidth=3, command=button_clr, activebackground='lightcoral', fg='white', bg='red', pady=10, font=('Courier', 10))
button_del=Button(root, text="CE ", padx=40, borderwidth=3, command=button_del, activebackground='grey', fg='black', bg='white', pady=10, font=('Courier', 10))
button_equal=Button(root, text="  =  ", padx=90, borderwidth=3, command=button_equal, activebackground='lightsky blue', fg='white', bg='darkblue', pady=10, font=('Courier', 10))

button_add=Button(root, text=" + ", padx=40, borderwidth=3, command=button_add, fg='white', bg='Grey', pady=10, font=('Courier', 10))
button_minus=Button(root, text=" - ", padx=40, borderwidth=3, command=button_minus, fg='white', bg='Grey', pady=10, font=('Courier', 10))
button_into=Button(root, text=" × ", padx=40, borderwidth=3, command=button_into, fg='white', bg='Grey', pady=10, font=('Courier', 10))
button_div=Button(root, text=" / ", padx=40, borderwidth=3, command=button_div, fg='white', bg='Grey', pady=10, font=('Courier', 10))



# Displaying Buttons
button0.grid(row=4, column=0, columnspan=3)

button1.grid(row=3, column=0)
button2.grid(row=3, column=1)
button3.grid(row=3, column=2)

button4.grid(row=2, column=0)
button5.grid(row=2, column=1)
button6.grid(row=2, column=2)

button7.grid(row=1, column=0)
button8.grid(row=1, column=1)
button9.grid(row=1, column=2)

button_del.grid(row=1, column=3)
button_clr.grid(row=1, column=4)
button_equal.grid(row=4, column=3, columnspan=2)

button_add.grid(row=3, column=3)
button_minus.grid(row=3, column=4)
button_into.grid(row=2, column=3)
button_div.grid(row=2, column=4)

root.mainloop()
