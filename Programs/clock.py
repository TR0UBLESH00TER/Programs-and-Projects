from tkinter import *
from time import strftime

root = Tk()
root.title("Clock")
root.geometry("500x400")
root.resizable(0,0)

frame = Frame(root)
frame.pack()

Label(frame,text="Clock",font=("Consolas",80)).grid(row=0,column=1)

def clock():
    time_now = strftime('%H:%M:%S') 
    date_now = strftime('%d-%m-%Y') 

    date.config(text = date_now)
    time.config(text = time_now)
    
    date.after(1000, clock)

time = Label(frame,font=("Consolas",50))
time.grid(row=1,column=1)
date = Label(frame,font=("Consolas",30))
date.grid(row=2,column=1)
clock()


root.mainloop()