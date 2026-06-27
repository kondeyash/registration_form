import tkinter as tk
from tkinter import messagebox
import mysql.connector


# Database Connection
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Yash@439226",
    database="student_db"
)

cursor = db.cursor()


def register():

    name = name_entry.get()
    email = email_entry.get()
    phone = phone_entry.get()
    gender = gender_entry.get()
    dob = dob_entry.get()
    course = course_entry.get()
    address = address_entry.get()


    query = """
    INSERT INTO students
    (name,email,phone,gender,dob,course,address)
    VALUES(%s,%s,%s,%s,%s,%s,%s)
    """

    data = (
        name,
        email,
        phone,
        gender,
        dob,
        course,
        address
    )


    cursor.execute(query,data)
    db.commit()


    messagebox.showinfo(
        "Success",
        "Student Registered Successfully"
    )


# Window

root = tk.Tk()
root.title("Student Registration Form")
root.geometry("400x500")


tk.Label(root,text="Student Registration",
         font=("Arial",18)).pack()


labels=[
"Name",
"Email",
"Phone",
"Gender",
"DOB",
"Course",
"Address"
]


entries=[]


for text in labels:

    tk.Label(root,text=text).pack()

    e=tk.Entry(root)
    e.pack()

    entries.append(e)


name_entry,email_entry,phone_entry,\
gender_entry,dob_entry,course_entry,address_entry = entries


tk.Button(
    root,
    text="Register",
    command=register
).pack(pady=20)


root.mainloop()