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

# Checking if setup.py was already run or not and display message to run main.py if it was already run.
try:
    with open(".\\data\\data.txt","r") as f:
        messagebox.showinfo("Alert","The setup was already completed. Please use \"main.py\"")
        quit()    # Closes the wndow
except Exception:
    # The code will continue
    f = ""

#Creating the window
login = Tk()
login.title(" Login")
login.iconbitmap(".\\data\\Data.ico")
login.geometry("600x400")
login.resizable(0,0)

def password():          # Function to accept & store password and create database "school_data"
    global pwd
    global frame
    global login
    pwd = e.get()
    try:
        db=mysql.connector.connect(host='localhost', user='root', passwd=pwd)
        if db.is_connected():
            
            c=db.cursor()
            c.execute("CREATE DATABASE school_data;")

            # Storing the password in a seperate file for later use
            with open(".\\data\\data.txt","w") as f:
                f.write(pwd)

            # Displaying success message
            messagebox.showinfo("Success","Successfully logged in and the database named \"school_data\" was created.")

            frame.destroy()
            login.title(" Setup")
            frame = LabelFrame(login,text="Setup",padx=20,pady=100,labelanchor=N)
            frame.pack(padx=20,pady=20)
            Button(frame,text="Create Tables",padx=40,pady=20,command=createtable).grid(row=0,column=0,padx=40,pady=40)
    except Exception:
        messagebox.showerror("Invalid Password","The password you have entered is incorrect.")
        e.delete(0, END) # Clearing the Entry box

def createtable():         # Function to create table in MySQL
    global pwd
    dbase=mysql.connector.connect(host='localhost', user='root', passwd=pwd, database='school_data')
    cursor=dbase.cursor()
    cursor.execute('CREATE TABLE student ( \
			    Admission_No INT(8) NOT NULL PRIMARY KEY AUTO_INCREMENT, \
			    Name VARCHAR(25) NOT NULL, \
			    Class INT(2) NOT NULL, \
			    Section VARCHAR(1) NOT NULL, \
			    Phone_No VARCHAR(10), \
			    DOB DATE, \
			    DOA DATE) ')
    cursor.close()
    messagebox.showinfo("Success","Table named \"student\" was created.")

    # Closing the window after completing the setup
    login.destroy()

# Creating frame for login
frame = LabelFrame(login,text="Setup",padx=20,pady=100,labelanchor=N)
frame.pack(padx=20,pady=20)

Label(frame,text="Enter password:").grid(row=0,column=0)

e = Entry(frame,width=50)
e.grid(row=0,column=1)
e.config(show="•")

pwd = ""                     #This variable will be used to store password

Button(frame,text="Submit",padx=5,command=password).grid(row=0,column=3)

login.mainloop()
