"""
Requirements:
Python
MySQL
Tkinter
mysql.connector
"""

from tkinter import *
from tkinter import messagebox
import mysql.connector

login = Tk()
login.title(" Login")
login.iconbitmap(".\\ico\\Data.ico")
login.geometry("600x400")
login.resizable(0,0)

frame = LabelFrame(login,text="Setup",padx=20,pady=100)
frame.pack(padx=20,pady=20)

Label(frame,text="Enter password:").grid(row=0,column=0)

e = Entry(frame,width=50)
e.grid(row=0,column=1)
e.config(show="*")

pwd = ""

def createdb():
    global pwd
    dbase=mysql.connector.connect(host='localhost', user='root', passwd=pwd, database='school_data')
    cursor=dbase.cursor()
    cursor.execute('CREATE TABLE student ( \
			    Admission_No INT NOT NULL PRIMARY KEY AUTO_INCREMENT, \
			    Name VARCHAR(25), \
			    Class INT, \
			    Section VARCHAR(1), \
			    Phone_No VARCHAR(10), \
			    DOB DATE, \
			    DOA DATE) ')
    cursor.close()
    messagebox.showinfo("Success","Table named \"student\" was created.")
    login.destroy()

def password():
    global pwd
    global frame
    global login
    pwd = e.get()
    e.delete(0, END)
    try:
        db=mysql.connector.connect(host='localhost', user='root', passwd=pwd)
        if db.is_connected():
            with open("data.txt","w") as f:
                f.write(pwd)
            c=db.cursor()
            c.execute("CREATE DATABASE school_data;")
            messagebox.showinfo("Success","Successfully logged in and the database named \"school_data\" was created.")
            frame.destroy()
            login.title(" Setup")
            frame = LabelFrame(login,text="Setup",padx=20,pady=100)
            frame.pack(padx=20,pady=20)
            Button(frame,text="Create Tables",padx=40,pady=20,command=createdb).grid(row=0,column=0,padx=40,pady=40)
    except EOFError:
        messagebox.showerror("Invalid Password","The password entered is INVALID.")

Button(frame,text="Submit",padx=5,command=password).grid(row=0,column=3)
login.mainloop()
