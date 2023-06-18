# Invoice Generator using tk

import tkinter as tk
from tkinter import ttk
from docxtpl import DocxTemplate
import datetime
from tkinter import messagebox

BLACK = '#000000'
WHITE = '#FFFFFF'
AUREOLIN = '#F8F32B'
COOL_GRAY = '#8D99AE'
SPACE_CADET = '#2B2D42'
LAVENDER = '#DBD2E0'
GREEN = '#58641D'
FONT = 'Helvetica'


def on_entry_add(event):
    add_item_button.configure(bg=COOL_GRAY)
    window.configure(cursor="hand2")

def on_leave_add(event):
    add_item_button.configure(bg=LAVENDER)
    window.configure(cursor="")

def on_entry_new(event):
    new_invoice_button.configure(bg=COOL_GRAY)
    window.configure(cursor="hand2")

def on_leave_new(event):
    new_invoice_button.configure(bg=LAVENDER)
    window.configure(cursor="")

def on_entry_save(event):
    save_invoice_button.configure(bg=GREEN, fg=WHITE)
    window.configure(cursor="hand2")

def on_leave_save(event):
    save_invoice_button.configure(bg=AUREOLIN,fg=BLACK)
    window.configure(cursor="")

def clear_item():
    qty_spinbox.delete(0, tk.END)
    qty_spinbox.insert(0, "1")
    desc_entry.delete(0, tk.END)
    price_spinbox.delete(0, tk.END)
    price_spinbox.insert(0, "0.0")

items = []
def add_item():
    qty = int(qty_spinbox.get())
    desc = desc_entry.get()
    price = float(price_spinbox.get())
    line_total = qty*price
    invoice_item = [qty, desc, price, line_total]
    tree.insert('',0, values=invoice_item)
    clear_item()
    
    items.append(invoice_item)

    
def new_invoice():
    first_name_entry.delete(0, tk.END)
    last_name_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    clear_item()
    tree.delete(*tree.get_children())
    
    items.clear()
    
def generate_invoice():
    doc = DocxTemplate("invoice_template.docx")
    name = first_name_entry.get()+last_name_entry.get()
    phone = phone_entry.get()
    subtotal = sum(item[3] for item in items) 
    tax = 0.18
    total = subtotal*(1-tax)
    
    doc.render({"name":name, 
            "phone":phone,
            "invoice_list": items,
            "subtotal":subtotal,
            "tax":str(tax*100)+"%",
            "total":total})
    
    doc_name = "new_invoice" + name + datetime.datetime.now().strftime("%Y-%m-%d-%H%M%S") + ".docx"
    doc.save(doc_name)
    
    messagebox.showinfo("Invoice Complete", "Invoice Complete")
    
    new_invoice()



# Creating the GUI window
window = tk.Tk()
window.title("Invoice Generator")
window.configure(bg=SPACE_CADET)
frame = tk.Frame(window, bg=SPACE_CADET)
frame.pack(padx=20, pady=10)

first_name_label = tk.Label(frame, text="First Name", font=(FONT, 12), bg=SPACE_CADET, fg=WHITE)
first_name_label.grid(row=0, column=0, pady=5)
last_name_label = tk.Label(frame, text="Last Name", font=(FONT, 12), bg=SPACE_CADET, fg=WHITE)
last_name_label.grid(row=0, column=1, pady=5)

first_name_entry = tk.Entry(frame,font=(FONT,12), border=0)
last_name_entry = tk.Entry(frame,font=(FONT,12), border=0)
first_name_entry.grid(row=1, column=0, pady=5)
last_name_entry.grid(row=1, column=1, pady=5)

phone_label = tk.Label(frame, text="Phone", font=(FONT,12), bg=SPACE_CADET, fg=WHITE)
phone_label.grid(row=0, column=2, pady=5)
phone_entry = tk.Entry(frame,font=(FONT,12), border=0)
phone_entry.grid(row=1, column=2, pady=5)

qty_label = tk.Label(frame, text="Quantity", font=(FONT,12), bg=SPACE_CADET, fg=WHITE)
qty_label.grid(row=2, column=0, pady=5)
qty_spinbox = tk.Spinbox(frame, from_=1, to=100,font=(FONT,12), border=0)
qty_spinbox.grid(row=3, column=0, pady=5)

desc_label = tk.Label(frame, text="Description", font=(FONT,12), bg=SPACE_CADET, fg=WHITE)
desc_label.grid(row=2, column=1, pady=5)
desc_entry = tk.Entry(frame,font=(FONT,12), border=0)
desc_entry.grid(row=3, column=1, pady=5)

price_label = tk.Label(frame, text="Unit Price", font=(FONT,12), bg=SPACE_CADET, fg=WHITE)
price_label.grid(row=2, column=2, pady=5)
price_spinbox = tk.Spinbox(frame, from_=0.0, to=500, increment=0.5,font=(FONT,12), border=0)
price_spinbox.grid(row=3, column=2, pady=5)

add_item_button = tk.Button(frame, text = "Add item", command = add_item, font=(FONT,12), bg = LAVENDER,activebackground=COOL_GRAY ,borderwidth=0, highlightthickness=0,relief='flat')
add_item_button.bind("<Enter>",on_entry_add)
add_item_button.bind("<Leave>",on_leave_add)
add_item_button.grid(row=4, column=2, pady=5)

def create_custom_treeview_theme():
    style = ttk.Style()

    # Configure the TreeView style
    style.theme_create("CustomTreeview", parent="alt", settings={
        "Treeview": {
            "configure": {
                "background": COOL_GRAY,  # Set the background color
                "foreground": BLACK,  # Set the text color
                "fieldbackground":COOL_GRAY
            },
            "map": {
                "background": [("selected", AUREOLIN)],  # Set the background color for selected rows
                "foreground": [('selected',BLACK)]
            }
        }
    })

    # Apply the custom theme to TreeView
    style.theme_use("CustomTreeview")

columns = ('qty', 'desc', 'price', 'total')
column_alignments = ('center', 'center', 'center', 'center')
tree = ttk.Treeview(frame, columns=columns, show="headings")
create_custom_treeview_theme()
for column, alignment in zip(columns, column_alignments):
    tree.heading(column, text=column.capitalize(), anchor=alignment)
    tree.column(column, anchor=alignment)
tree.heading('qty', text='Qty')
tree.heading('desc', text='Description')
tree.heading('price', text='Unit Price')
tree.heading('total', text="Total")

    
tree.grid(row=5, column=0, columnspan=3, padx=20, pady=10)


save_invoice_button = tk.Button(frame, text="Generate Invoice", command=generate_invoice, borderwidth=0,highlightthickness=0, bg=AUREOLIN, relief='flat', font=(FONT,12))
save_invoice_button.grid(row=6, column=0, columnspan=3, sticky="news", padx=20, pady=5)
save_invoice_button.bind("<Enter>", on_entry_save)
save_invoice_button.bind("<Leave>", on_leave_save)
new_invoice_button = tk.Button(frame, text="New Invoice", command=new_invoice,font=(FONT,12) ,borderwidth=0, highlightthickness=0,relief='flat',bg=LAVENDER)
new_invoice_button.grid(row=7, column=0, columnspan=3, sticky="news", padx=20, pady=5)
new_invoice_button.bind("<Enter>", on_entry_new)
new_invoice_button.bind("<Leave>", on_leave_new)

window.mainloop()