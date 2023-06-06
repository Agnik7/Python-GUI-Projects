"""
 API used: tinyurl API

 Library to install: pyshorteners

"""

# Import necessary libraries
import tkinter as tk
import pyshorteners as ps
import pyperclip as pc
from tkinter import messagebox
# Initializing the window and the frame
window = tk.Tk()
window.title("Simple URL Shortener")
window.geometry('640x480')
window.configure(bg='#f2c4b8')
frame = tk.Frame(bg='#f2c4b8')

# Defining the reduce() function
def reduce():
    shortener = ps.Shortener()
    url = shortener.tinyurl.short(input_entry.get())
    output_entry.delete(0, tk.END)
    output_entry.insert(0, url)
    if url:
        copy_button.grid(row=2, column=2, columnspan=2,padx=10)
    else:
        copy_button.grid_forget()


#defining the function to copy the link to clipboard
def copy_to_clipboard():
    url = output_entry.get()
    pc.copy(url)
    messagebox.showinfo(title="Text Copy", message="Copied!!")
    input_entry.delete(0, tk.END) # Clears the input_entry field
    output_entry.delete(0, tk.END) # Clears the output_entry field


#defining the hover effects for generating button
def on_enter(event):
    button.configure(bg='#19184d', fg='#87b1ac')
    window.config(cursor="hand2")

def on_leave(event):
    button.configure(bg='#87b1ac', fg='#19184d')
    window.config(cursor="")

#defining the hover effects for the copy
def copy_on_enter(event):
    copy_button.configure(bg='#19184d', fg='#87b1ac')
    window.config(cursor="hand2")
def copy_on_leave(event):
    copy_button.configure(bg='#87b1ac', fg='#19184d')
    window.config(cursor="")

# Stating the Labels of the widgets
title = tk.Label(frame,text="URL Shortener",bg='#f2c4b8', fg='#1b227d', font=("Arial",30, "bold", "underline"))
input_label = tk.Label(frame, text = "Enter URL:",bg='#f2c4b8', fg='#1b227d',font=("Arial",20))
input_entry = tk.Entry(frame, fg='#1b227d',font=("Arial",20))
output_label = tk.Label(frame,text="Shortened URL:",bg='#f2c4b8', fg='#1b227d',font=("Arial",20))
output_entry = tk.Entry(frame, fg='#1b227d',font=("Arial",20))
button = tk.Button(frame, bg = '#87b1ac',fg='#19184d',text="Shorten", command=reduce,font=("Arial",20),borderwidth=0, highlightthickness=0, relief="flat")
button.bind("<Enter>", on_enter)
button.bind("<Leave>", on_leave)
copy_button = tk.Button(frame, bg='#87b1ac', fg='#19184d', text="Copy", command=copy_to_clipboard, font=("Arial", 15), borderwidth=0, highlightthickness=0, relief="flat")
copy_button.bind("<Enter>", copy_on_enter)
copy_button.bind("<Leave>", copy_on_leave)

# Positioning and styling the widgets within the frame using grid
title.grid(row=0, column=0, columnspan=2, sticky="news", pady=50)
input_label.grid(row=1, column=0, pady=20, padx=20)
input_entry.grid(row=1, column=1)
output_label.grid(row=2, column=0, pady=20, padx=20)
output_entry.grid(row=2, column=1)
button.grid(row=3, column=0, columnspan=2)
copy_button.grid(row=2, column=2, columnspan=2, padx= 10)
copy_button.grid_forget()

#displaying the frame using pack()
frame.pack()

window.mainloop()
