"""
Requirements:
- Python
- Tkinter
- Mysql-connector
- MySQL
"""

from tkinter import *
from tkinter import messagebox
import mysql.connector
import csv

# Getting the password obtained in "setup.py" and showing error if "setup.py" wasn't run.
try:
    with open(".\\data\\data.txt", "r") as f:
        pwd = f.read()
    # Connecting to Mysql database and creationg cursor
    db=mysql.connector.connect(host='localhost', user='root', passwd=pwd, database='school_data')
    cursor=db.cursor()

except:
    messagebox.showerror("Error", "Run \"setup.py\" before running this file.")
    quit()
if pwd == "":
    messagebox.showerror("Error", "Run \"setup.py\" before running this file.")
    quit()

# Declaring global variables to use in functions
name, _class, section, phone, dob, doa, delete, edit, search, col, data = '', '', '', '', '', '', '', '', '', [], []

# Function of main menu
def menu():
    global frame
    frame.destroy()        # Clears screen
    frame = LabelFrame(root,text=" Menu ",font=('Courier'),padx=200,pady=160,labelanchor=N)
    frame.pack(padx=20,pady=20)
    Button(frame, text='Enter Student Record ', font=('Courier', 10), padx=20, command=Enter).grid(row=0, column=0, pady=5)
    Button(frame, text='Display Student Data ', font=('Courier', 10), padx=20, command=display).grid(row=1, column=0, pady=5)
    Button(frame, text='Edit Student Record  ', font=('Courier', 10), padx=20, command=edit_menu).grid(row=2, column=0, pady=5)
    Button(frame, text='Delete Student Record', font=('Courier', 10), padx=20, command=del_menu).grid(row=3, column=0, pady=5)
    Button(frame, text='        Quit         ', font=('Courier', 10), padx=20, command=quit).grid(row=4, column=0, pady=5)

# Function to Accept Student Record
def Enter():
    global frame, name, _class, section, phone, dob, doa
    frame.destroy()        # Clears screen
    frame = LabelFrame(root, text=" Enter Data ", font=('Courier'), padx=50, pady=50, labelanchor=N)
    frame.pack(padx=20, pady=20)

    # Button to get back to main menu
    Button(frame, text='Back', font=('Courier', 10),padx=50,command=menu).grid(row=0, column=0, pady=5)

    Label(frame, text='Student Data', font=('Courier', 20)).grid(row=1, column=0, pady=5, columnspan=2)
    Label(frame, text='Name             ', font=('Courier', 10)).grid(row=2, column=0, pady=5)
    Label(frame, text='Class            ', font=('Courier', 10)).grid(row=3, column=0, pady=5)
    Label(frame, text='Section          ', font=('Courier', 10)).grid(row=4, column=0, pady=5)
    Label(frame, text='Phone No         ', font=('Courier', 10)).grid(row=5, column=0, pady=5)
    Label(frame, text='D.O.B(YYYY-MM-DD)', font=('Courier', 10)).grid(row=6, column=0, pady=5)
    Label(frame, text='D.O.A(YYYY-MM-DD)', font=('Courier', 10)).grid(row=7, column=0, pady=5)

    # Entries for filling records
    name = Entry(frame, width=40, font=('Courier', 10), borderwidth=3)
    name.grid(row=2, column=1, pady=5)

    _class = Entry(frame, width=40, font=('Courier', 10), borderwidth=3)
    _class.grid(row=3, column=1, pady=5)

    section = Entry(frame, width=40, font=('Courier', 10), borderwidth=3)
    section.grid(row=4, column=1, pady=5)

    phone = Entry(frame, width=40, font=('Courier', 10), borderwidth=3)
    phone.grid(row=5, column=1, pady=5)

    dob = Entry(frame, width=40, font=('Courier', 10), borderwidth=3)
    dob.grid(row=6, column=1, pady=5)

    doa = Entry(frame, width=40, font=('Courier', 10), borderwidth=3)
    doa.grid(row=7, column=1, pady=5)

    # Button to save in database
    Button(frame, text='Save', font=('Courier', 10),padx=100,command=save).grid(row=8, column=1, pady=5)

#Function that will save the records entered in Enter() [line 37] to MySQL database 
def save():
    global name, _class, section, phone, dob, doa, db, cursor
    try:
        # Fetching records entered in Enter()  [line 37]
        NAME = str(name.get())
        CLASS = str(_class.get())
        SECT = str(section.get())
        PHONE = str(phone.get())
        if len(PHONE) != 10:     # Raises error if number of digits in phone number is not 10
            raise Exception
        DOB=str(dob.get())
        DOA=str(doa.get())

        # Adding enterd records to MySQL Database
        query=f'INSERT INTO student(Name, Class, Section, Phone_No, DOB, DOA) VALUES(\'{NAME}\', {CLASS}, \'{SECT}\', {PHONE}, \'{DOB}\',\'{DOA}\')'
        cursor.execute(query)
        db.commit()

        # Clearing Entry boxes
        name.delete(0, END)
        _class.delete(0, END)
        section.delete(0, END)
        phone.delete(0, END)
        dob.delete(0, END)
        doa.delete(0, END)
 
        messagebox.showinfo('Success', 'Data sucessfully added')            # Showing success message

    except Exception:
        messagebox.showerror('Error', 'Please fill details in Valid way.')  # Showing error message

# Function to Display Records
def display():
    global pwd, frame, col, data, db, cursor,search
    frame.destroy()        # Clears screen
    frame = LabelFrame(root,text=" Student Details ",font=('Courier'),padx=10,pady=10,labelanchor=N)
    frame.pack(padx=20,pady=20)
    
    # Getting all records present in the Table "student"
    cursor.execute('SELECT * FROM student')
    data = cursor.fetchall()

    # Button to get back to main menu
    Button(frame, text='Back', font=('Courier', 10),padx=15,command=menu).grid(row=0, column=0, pady=5)

    Label(frame, text='  Search by Entering Admission Number', font=('Courier', 10)).grid(row=0, column=1, pady=5, columnspan=3)

    # Entry widget to get details of specified Admission_No
    search = Entry(frame,width=17)
    search.grid(row=0,column=4)
    Button(frame, text='Search', font=('Courier', 10),padx=15,command=Search).grid(row=0, column=5, pady=5)

    # Button to generate csv file of all data
    Button(frame, text='Get csv', font=('Courier', 10),padx=15,command=export_csv).grid(row=0, column=6)

    # Displaying Column Names
    i = 2
    col = ['Admission No','Name','Class','Section','Phone Number','DOB','DOA']
    for j in range(len(col)):
        e = Entry(frame, width=17) 
        e.grid(row=1, column=j) 
        e.insert(END, col[j])

    # Displaying Data in the form of Table using Entry widget
    for student in data: 
        for j in range(len(student)):
            e = Entry(frame, width=17) 
            e.grid(row=i, column=j) 
            e.insert(END, student[j])
        i=i+1

# Function to serch and display records of Admission Number specified in display() [line 109]
def Search():
    global frame, db, cursor, search , data,name, _class, section, phone, dob, doa

    try:
        search = search.get()    # Fetching the Adimission number entered in Entry widget "search" [line 125]
        cursor.execute(f'SELECT * FROM student WHERE Admission_No = {search}')
        data = cursor.fetchone()
        if data == None:
            raise Exception      # Causes Error if Record for specified Admission Number not present in student table

        frame.destroy()        # Clears screen

        frame = LabelFrame(root, text=" Student Record ", font=('Courier'), padx=50, pady=50, labelanchor=N)
        frame.pack(padx=20, pady=20)

        # Button to go back to previous Display window
        Button(frame, text='Back', font=('Courier', 10),padx=50,command=display).grid(row=0, column=0, pady=5)

        # Displaying the record of specified Admission Number
        Label(frame, text='Name     ', font=('Courier', 10)).grid(row=2, column=0, pady=5)
        Label(frame, text='Class    ', font=('Courier', 10)).grid(row=3, column=0, pady=5)
        Label(frame, text='Section  ', font=('Courier', 10)).grid(row=4, column=0, pady=5)
        Label(frame, text='Phone No ', font=('Courier', 10)).grid(row=5, column=0, pady=5)
        Label(frame, text='D.O.B    ', font=('Courier', 10)).grid(row=6, column=0, pady=5)
        Label(frame, text='D.O.A    ', font=('Courier', 10)).grid(row=7, column=0, pady=5)

        name = Entry(frame, width=40, font=('Courier', 10), borderwidth=3)
        name.grid(row=2, column=1, pady=5)
        name.insert(END, data[1])

        _class = Entry(frame, width=40, font=('Courier', 10), borderwidth=3)
        _class.grid(row=3, column=1, pady=5)
        _class.insert(END, data[2])

        section = Entry(frame, width=40, font=('Courier', 10), borderwidth=3)
        section.grid(row=4, column=1, pady=5)
        section.insert(END, data[3])

        phone = Entry(frame, width=40, font=('Courier', 10), borderwidth=3)
        phone.grid(row=5, column=1, pady=5)
        phone.insert(END, data[4])

        dob = Entry(frame, width=40, font=('Courier', 10), borderwidth=3)
        dob.grid(row=6, column=1, pady=5)
        dob.insert(END, data[5])

        doa = Entry(frame, width=40, font=('Courier', 10), borderwidth=3)
        doa.grid(row=7, column=1, pady=5)
        doa.insert(END, data[6])

    except Exception:
        display()
        messagebox.showerror('Error','Please enter valid Admission number')
    
#Function to generate csv file of the records present in the student table
def export_csv():
    global col,data
    with open('Student_Data.csv', 'a',newline="") as f:
        writer=csv.writer(f)
        writer.writerow(col)
        for i in data:
            writer.writerow(i)

        messagebox.showinfo('Exported', 'Data exported successfully')

# Edit menu to accept Admission number to edit record
def edit_menu():
    global frame, delete, edit
    frame.destroy()        # Clears screen
    frame = LabelFrame(root, text=" Edit Record ", font=('Courier'), padx=50, pady=50, labelanchor=N)
    frame.pack(padx=20, pady=20)
    Button(frame, text='Back', font=('Courier', 10),padx=50,command=menu).grid(row=0, column=0, pady=5)

    Label(frame,text="Enter Admission number to edit:").grid(row=1,column=0)

    edit= Entry(frame,width=50)
    edit.grid(row=1,column=1)

    Button(frame, text='Edit', font=('Courier', 10),padx=100, command=Edit).grid(row=2, column=1, pady=20)

# Function to Edit data of a particular person based on provided Admission number
def Edit():
    global frame, db, cursor, edit, data,name, _class, section, phone, dob, doa

    try:
        # Fetching the existing record from the table "student" 
        edit = edit.get()
        cursor.execute(f'SELECT * FROM student WHERE Admission_No = {edit}')
        data = cursor.fetchone()
        if data == None:
            raise Exception

        frame.destroy()        # Clears screen

        frame = LabelFrame(root, text=" Edit Record ", font=('Courier'), padx=50, pady=50, labelanchor=N)
        frame.pack(padx=20, pady=20)

        # Button to go back to previous Edit window
        Button(frame, text='Back', font=('Courier', 10),padx=50,command=edit_menu).grid(row=0, column=0, pady=5)

        Label(frame, text='Name             ', font=('Courier', 10)).grid(row=2, column=0, pady=5)
        Label(frame, text='Class            ', font=('Courier', 10)).grid(row=3, column=0, pady=5)
        Label(frame, text='Section          ', font=('Courier', 10)).grid(row=4, column=0, pady=5)
        Label(frame, text='Phone No         ', font=('Courier', 10)).grid(row=5, column=0, pady=5)
        Label(frame, text='D.O.B(YYYY-MM-DD)', font=('Courier', 10)).grid(row=6, column=0, pady=5)
        Label(frame, text='D.O.A(YYYY-MM-DD)', font=('Courier', 10)).grid(row=7, column=0, pady=5)

        #Entries to make changes to existing data
        name = Entry(frame, width=40, font=('Courier', 10), borderwidth=3)
        name.grid(row=2, column=1, pady=5)
        name.insert(END, data[1])

        _class = Entry(frame, width=40, font=('Courier', 10), borderwidth=3)
        _class.grid(row=3, column=1, pady=5)
        _class.insert(END, data[2])

        section = Entry(frame, width=40, font=('Courier', 10), borderwidth=3)
        section.grid(row=4, column=1, pady=5)
        section.insert(END, data[3])

        phone = Entry(frame, width=40, font=('Courier', 10), borderwidth=3)
        phone.grid(row=5, column=1, pady=5)
        phone.insert(END, data[4])

        dob = Entry(frame, width=40, font=('Courier', 10), borderwidth=3)
        dob.grid(row=6, column=1, pady=5)
        dob.insert(END, data[5])

        doa = Entry(frame, width=40, font=('Courier', 10), borderwidth=3)
        doa.grid(row=7, column=1, pady=5)
        doa.insert(END, data[6])

        # Buttons to save changes in database
        Button(frame, text='Save Changes', font=('Courier', 10),padx=100,command=edit_save).grid(row=8, column=1, pady=5)

    except Exception:
        edit.delete(0,END)
        messagebox.showerror('Error','Please enter valid Admission number')

# Function to save edit changes in the MySQL database
def edit_save():
    global name, _class, section, phone, dob, doa, db, cursor, edit, frame
    data = [name.get(), _class.get(), section.get(), phone.get(), dob.get(), doa.get()]
    query = f"UPDATE student SET Name = \'{data[0]}\', Class = {data[1]}, Section = \'{data[2]}\', Phone_No = {data[3]}, DOB = \'{data[4]}\', DOA = \'{data[5]}\' WHERE Admission_No = {edit}"
    cursor.execute(query)
    db.commit()
    messagebox.showinfo("Success","Record updated successfully")
    edit_menu()

# Edit menu to accept Admission number to delete all records
def del_menu():
    global frame, delete
    frame.destroy()        # Clears screen
    frame = LabelFrame(root, text=" Delete Reccord ", font=('Courier'), padx=50, pady=50, labelanchor=N)
    frame.pack(padx=20, pady=20)

    # Button to go back to main menu
    Button(frame, text='Back', font=('Courier', 10),padx=50,command=menu).grid(row=0, column=0, pady=5)

    Label(frame,text="Enter Admission number to delete:").grid(row=1,column=0)

    delete= Entry(frame,width=50)     # Accepts Admission Number
    delete.grid(row=1,column=1)

    Button(frame, text='Delete', font=('Courier', 10),padx=100, command=Delete).grid(row=2, column=1, pady=20)

# Function to Delete data of a particular person based on provided Admission number
def Delete():
    global pwd, delete, frame, db, cursor
    DELETE = delete.get()
    try:
        cursor.execute(f'DELETE FROM student WHERE Admission_No ={DELETE}')
        db.commit()
        delete.delete(0, END)
        if cursor.rowcount == 0:
            raise Exception             # Raises Error if 0 rows were affected i.e., Admission No not present
        messagebox.showinfo('Deleted', 'Record deleted successfully')

    except Exception:
        messagebox.showerror('Error', 'Admission Number not found')


# Creating Window
root = Tk()
root.title(" Menu")
root.iconbitmap(".\\data\\Database.ico")
root.geometry("800x600")

frame = LabelFrame(root,text=" Menu ",font=('Courier'),padx=200,pady=200,labelanchor=N)
frame.pack(padx=20,pady=20)
menu()

root.mainloop()
