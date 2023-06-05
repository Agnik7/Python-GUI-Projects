# Importing necessary libraries
import tkinter as tk
from tkinter import messagebox #It needs to be imported explicitly to work

# Initializing the window and the frame
window = tk.Tk()
window.title("Simple Login Form")
window.geometry('640x480') # width x height
window.configure(bg='#212121')
frame = tk.Frame(bg='#212121')

# Function to show popup
def login():
    username="johndoe"
    password="12345"
    if(username_entry.get() == username and password_entry.get() == password):
        print("Login Successful")
        messagebox.showinfo(title="Login Successful!", message="Welcome John Doe!!")
    else:
        print("Login Failed")
        messagebox.showinfo(title="Login Failed!", message="Invalid Credentials")

# Stating the Labels of the frame, username, password and button

login_label = tk.Label(frame, text= "Login Form",bg='#212121', fg='#ffffff', font=("Arial",30))
username_label= tk.Label(frame, text= "Username",bg='#212121', fg='#ffffff', font=("Arial",18))
username_entry = tk.Entry(frame, font=("Arial",18))
password_label= tk.Label(frame, text= "Password",bg='#212121', fg='#ffffff', font=("Arial",18))
password_entry = tk.Entry(frame, show="*",font=("Arial",18))
login_button = tk.Button(frame,text="Login", bg='#0598ed', fg='#ffffff', font=("Arial",18), command=login)

# Positioning and styling the widgets within the frame using grid

login_label.grid(row=0, column=0, columnspan=2, sticky="news", pady=40)
username_label.grid(row=1,column=0)
username_entry.grid(row=1,column=1, pady=20)
password_label.grid(row=2,column=0)
password_entry.grid(row=2,column=1, pady=20)
login_button.grid(row=3 ,column=0, columnspan=2, pady=30)

# Displaying the frame using pack()

frame.pack()

window.mainloop()
