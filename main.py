#                                                                  PHONE DIRECTORY

# libraries
from tkinter import *
import tkinter.messagebox as mb
import mysql.connector

# database Connection (Please enter your database credentials)
mydb = mysql.connector.connect(host="*****", user="*****", password="*****",
                               auth_plugin='mysql_native_password')
cursor = mydb.cursor()
cursor = mydb.cursor(buffered=True)

# DATABASE queries
cursor.execute("CREATE DATABASE IF NOT EXISTS PHONE_DIRECTORY")
cursor.execute("USE PHONE_DIRECTORY")
cursor.execute("CREATE TABLE IF NOT EXISTS RECORDS(Name varchar(30),"
               " Mobile varchar(15), Work varchar(15), PRIMARY KEY (Mobile))")

# window
root = Tk()

# window geometry(SIZE)
root.title("Phone-Directory")
root.geometry('500x750')
root.resizable(width=1, height=1)

# colors
lf_bg = 'white'

# font style
frame_font = ("Garamond", 14, 'bold')

# StringVar objects
name_str = StringVar()
phone_str = StringVar()
work_str = StringVar()
search_str = StringVar()

# header label(contacts)
Label(root, text="Contacts", font=("Noto Sans CJK TC", 30, "bold"), bg='lime green', fg='Black').pack(side=TOP, fill=X)

# frames
upp_frame = Frame(root, bg=lf_bg)
low_frame = Frame(root, bg=lf_bg)

# frames setting
upp_frame.place(rely=0.07, relheight=0.3, x=0, relwidth=1)
low_frame.place(rely=0.35, relheight=1, x=0, relwidth=1)

# labels
# name label and entry section
Label(upp_frame, text="Name", font=frame_font, bg="white").place(relx=0.05, rely=0.06)
name = Entry(upp_frame, width=20, font=("Garamond", 11), bg="gainsboro", textvariable=name_str)
name.place(relx=0.22, rely=0.07)

# mobile label and entry section
Label(upp_frame, text="Mobile", font=frame_font, bg="white").place(relx=0.05, rely=0.28)
Mobile = Entry(upp_frame, width=20, font=("Garamond", 11), bg="gainsboro", textvariable=phone_str)
Mobile.place(relx=0.22, rely=0.30)

# work label and entry section
Label(upp_frame, text="Work", font=frame_font, bg="white").place(relx=0.05, rely=0.50)
Work = Entry(upp_frame, width=20, font=("Garamond", 11), bg="gainsboro", textvariable=work_str)
Work.place(relx=0.22, rely=0.50)

# search entry section
Search = Entry(upp_frame, width=20, font=("Garamond", 11), bg="gainsboro", textvariable=search_str)
Search.insert(END, 'Enter Name')
Search.pack()
Search.place(relx=0.65, rely=0.15)


# records label
Label(low_frame, text="Records", font=frame_font, bg='lime green').pack(fill=X)

# listbox and scroller
listbox = Listbox(low_frame, selectbackground='SkyBlue', bg='Gainsboro', font=('Helvetica', 12), height=20, width=50)
scroller = Scrollbar(listbox, orient=VERTICAL, command=listbox.yview)
scroller.place(relx=0.96, rely=0, relheight=1)
# listbox.config(yscrollcommand=scroller.set)
listbox.place(relx=0.05, rely=0.05)


# functions
# adding contacts iin database
def add():
    global name_str, phone_str, work_str
    global cursor
    Name, phone, work = name_str.get(), phone_str.get(), work_str.get()
    if Name == "" or phone == "":
        mb.showerror("ERROR", "Name or Mobile not be empty")
    else:
        cursor.execute("INSERT INTO RECORDS(NAME, MOBILE , WORK) VALUES(%s, %s, %s)", (Name, phone, work))
        mydb.commit()
        mb.showinfo("DONE", "Contact saved successfully")
        listbox.delete(0, END)
        name_str.set('')
        phone_str.set('')
        work_str.set('')
        List_contact()


# list_contacts in listbox
def List_contact():
    global cursor
    cursor.execute("SELECT * FROM RECORDS")
    for x in cursor:
        listbox.insert(END, x)


# deleting contacts from database
def delete():
    global listbox
    if not listbox.get(ACTIVE):
        mb.showerror("No contact selected", "Please select an contact")
    else:
        cursor.execute("DELETE FROM RECORDS WHERE NAME= %s OR MOBILE = %s OR WORK = %s", (listbox.get(ACTIVE)))
        mydb.commit()
        mb.showinfo("Delete", "Contact deleted successfully")
        listbox.delete(0, END)
        List_contact()


# showing all contacts
def show():
    listbox.delete(0, END)
    cursor.execute("SELECT * FROM RECORDS")
    for x in cursor:
        listbox.insert(END, x)


# contact update
def update():
    global name_str, phone_str, work_str, cursor
    Name, phone, work = name_str.get(), phone_str.get(), work_str.get()
    if name != "" and work != "":
        cursor.execute("UPDATE RECORDS SET MOBILE = %s WHERE NAME = %s AND WORK = %s", (phone, Name, work))
        mydb.commit()
        mb.showinfo("UPDATE", "Contact changes successfully")
        listbox.delete(0, END)
        List_contact()
    else:
        mb.showerror("Error", "Please enter name and work details")


# searching contacts from database
def search():
    listbox.delete(0, END)
    global cursor
    query = (search_str.get())
    if query != "":
        cursor.execute("SELECT * FROM RECORDS WHERE NAME = %s", (query,))
        mydb.commit()
        data = cursor.fetchall()
        for x in data:
            listbox.insert(END, x)
        search_str.set("")
    else:
        mb.showerror("Error", "Please Enter name")


# buttons
Button(upp_frame, text="Search", font=frame_font, bg='lime green', width=8, command=lambda: search()).place(relx=0.70, rely=0.30)
Button(upp_frame, text="Add", font=frame_font, bg='lime green', width=5, command=lambda: add()).place(relx=0.10, rely=0.70)
Button(upp_frame, text="Update", font=frame_font, bg='lime green', width=8, command=lambda: update()).place(relx=0.27, rely=0.70)
Button(upp_frame, text="Delete", font=frame_font, bg='lime green', width=8, command=lambda: delete()).place(relx=0.51, rely=0.70)
Button(upp_frame, text="Show", font=frame_font, bg='lime green', width=7, command=lambda: show()).place(relx=0.75, rely=0.70)

# mainloop
root.mainloop()
