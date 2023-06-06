# Import necessary libraries
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import sqlite3

# Initializing the window and the frame
window = tk.Tk()
window.title("Data Entry")
window.geometry('640x480')
frame = tk.Frame(window)

# Define the function
def add_data():
    if(tc_accept.get() == "Not Accepted"):
        messagebox.showerror(title= "Error", message = "Please Accept the Terms and Conditions")
    else:
        first_name= first_name_entry.get()
        last_name = last_name_entry.get()
        title = title_combobox.get()
        gender = gender_combobox.get()
        age = age_spinbox.get()
        nationality = nationality_combobox.get()
        status = register_status.get()
        course = courses_spinbox.get()
        sem = sem_spinbox.get()
        print("First Name: " + first_name + "\tLast Name: " + last_name + "\tGender: " + gender)
        print("\nTitle: " + title + "\tAge: " + age + "\tNationality: " + nationality)
        print("\nCourses Completed: " + course+"\tSemester Completed: " + sem)
        print("\nRegistration Status: " + status)
        print("\n--------------------------------------------------------")

        # Creating Table
        connect = sqlite3.connect('database.db') # Connecting to database
        query = '''CREATE TABLE IF NOT EXISTS Student_data
                (title TEXT, firstname TEXT, lastname TEXT, gender TEXT, age INT, nationality TEXT, registration_status TEXT, courses INT, semesters INT)
        '''
        connect.execute(query) # Creating the table if it is not present

        #Inserting data
        data_insert = '''INSERT INTO Student_data (title, firstname, lastname, gender, age, nationality, registration_status, courses, semesters) VALUES (?,?,?,?,?,?,?,?,?)'''
        data_tuple = (title,first_name, last_name, gender, age, nationality, status, course, sem)

        cursor = connect.cursor()
        cursor.execute(data_insert, data_tuple)
        connect.commit() # Adding the data to the table
        connect.close()
        messagebox.showinfo(title= "Success", message = "Data Added Successfully!!")


# Getting the user info
user_info_frame = tk.LabelFrame(frame, text="User Information")
user_info_frame.grid(row=0, column=0, padx = 20, pady = 10)

first_name_label = tk.Label(user_info_frame, text="First Name")
first_name_entry= tk.Entry(user_info_frame)
last_name_label = tk.Label(user_info_frame, text="Last Name")
last_name_entry = tk.Entry(user_info_frame)
title_label = tk.Label(user_info_frame, text= "Title")
title_combobox = ttk.Combobox(user_info_frame, values=["", "Mr.", "Mrs.", "Dr."])
gender_label = tk.Label(user_info_frame, text="Gender")
gender_combobox = ttk.Combobox(user_info_frame, values=["Male", "Female", "Other", "Prefer Not to Say"])
age_label = tk.Label(user_info_frame, text="Age")
age_spinbox = tk.Spinbox(user_info_frame, from_=0, to=110)
nationality_label = tk.Label(user_info_frame, text="Nationality")
nationality_combobox = ttk.Combobox(user_info_frame, values=["India", "USA", "Australia", "England"])

first_name_label.grid(row=0,column=0)
last_name_label.grid(row=0,column=1)
first_name_entry.grid(row=1,column=0)
last_name_entry.grid(row=1,column=1)
title_label.grid(row=0,column=2)
title_combobox.grid(row=1,column=2)
gender_label.grid(row=2,column=0)
gender_combobox.grid(row=3,column=0)
age_label.grid(row=2,column=1)
age_spinbox.grid(row=3,column=1)
nationality_label.grid(row=2,column=2)
nationality_combobox.grid(row=3,column=2)

for widget in user_info_frame.winfo_children():
    widget.grid_configure(padx=10,pady=5)


# Getting Course Info
course_frame = tk.LabelFrame(frame, text="Course Information")

register_label = tk.Label(course_frame, text="Registration Status")
register_status = tk.StringVar(value="Not Registered")
register_check = tk.Checkbutton(course_frame, text="Currently Registered", variable=register_status, onvalue="Registerd", offvalue="Not Registered")
courses_label = tk.Label(course_frame, text="Courses Completed")
courses_spinbox = tk.Spinbox(course_frame, from_=0, to='infinity')
sem_label = tk.Label(course_frame, text="Semesters Completed")
sem_spinbox = tk.Spinbox(course_frame, from_=0, to='infinity')

register_label.grid(row=0,column=0)
register_check.grid(row=1,column=0)
courses_label.grid(row=0, column=1)
courses_spinbox.grid(row=1,column=1)
sem_label.grid(row=0, column=2)
sem_spinbox.grid(row=1,column=2)

for widget in course_frame.winfo_children():
    widget.grid_configure(padx=15,pady=5)

course_frame.grid(row=1, column=0, sticky="news", padx=20,pady=10)

# Terms and Conditions
tc_frame= tk.LabelFrame(frame, text="Terms&Conditions")
tc_accept = tk.StringVar(value="Not Accepted")
tc_checkbox = tk.Checkbutton(tc_frame, text="I Accept the Terms&Conditions", variable=tc_accept, onvalue="Accepted",offvalue="Not Accepted")

tc_frame.grid(row=0,column=0)

tc_checkbox.grid(row=1,column=0)
tc_frame.grid(row=2,column=0,sticky="news",padx=20,pady=10)

# Button
button = tk.Button(frame, text="Enter Data", command=add_data)
button.grid(row=3,column=0, sticky="news",padx=20,pady=5)

frame.pack()
window.mainloop()