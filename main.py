from tkinter import *
from tkinter import messagebox # Not a Class
from pyperclip import copy
from password import generate_password
import sys, os
import json

# Functions
def create_text_file():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if len(website_entry.get()) == 0 or len(password_entry.get()) == 0:
        messagebox.showwarning(title="empty fields", message="Please fill in all the required fields!")

    else:
        try:
            with open("password_manager.json", "r") as file:
                # Reading old data
                data = json.load(file)

        except FileNotFoundError:
            with open("password_manager.json", "w") as file:
                json.dump(new_data, file, indent = 4)
        
        else:
            # Updating old data with new data
            data.update(new_data)

            with open("password_manager.json", "w") as file:
                # Saving updated data
                json.dump(data, file, indent = 4)

        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)

def find_password():
    try:
        with open("password_manager.json", "r") as file:
            # Reading old data
            data = json.load(file)

    except FileNotFoundError:
        messagebox.showerror(title="File Not Found", message="No data file located")
    
    else:
        website = website_entry.get()
        website_list = [web.lower() for web in list(data.keys())]

        if website.lower() in website_list:
            messagebox.showinfo(title = website, message= f'email: {data[website]["email"]}\npassword: {data[website]["password"]}')
        else:
            messagebox.showinfo(title = website, message= f"Website {website} not found")


def get_path(filename):
    if hasattr(sys, "_MEIPASS"):
        return os.path.join(sys._MEIPASS, filename)
    else:
        return filename

def create_password():
    password = generate_password()
    password_entry.delete(0,END)
    password_entry.insert(0, password)
    copy(password)

# Window
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)
window.resizable(False, False)

# Canvas
lock_png = PhotoImage(file = get_path("logo.png"))
canvas = Canvas(height=200, width=200)
lock_image = canvas.create_image(100, 100,image = lock_png)
canvas.grid(column=1,row=0)

# Labels
website_label = Label(text = "Website:")
website_label.grid(column = 0, row = 1)

email_label = Label(text = "Email/Username:")
email_label.grid(column = 0, row = 2)

password_label = Label(text = "Password:")
password_label.grid(column = 0, row = 3)

# Entry
website_entry = Entry(width=35)
website_entry.grid(column = 1, row= 1, columnspan=2, sticky="ew")
website_entry.focus()

email_entry = Entry(width=35)
email_entry.grid(column = 1, row= 2, columnspan=2, sticky="ew")
email_entry.insert(END, "example@gmail.com")

password_entry = Entry(width = 20)
password_entry.grid(column = 1, row= 3, sticky="ew")

# Buttons
BACKGROUND = "lightgrey"

password_button = Button(text = "Generate Password", borderwidth=0.1, border=0.1, width = 16, command=create_password, background = BACKGROUND)
password_button.grid(column = 2, row = 3)

add_button = Button(text = "Add", width=30, borderwidth=0.1, border=0.1, command=create_text_file, background = BACKGROUND)
add_button.grid(column = 1, row = 4, columnspan=2, sticky="ew")

search_button = Button(text = "Search", width=16, borderwidth=0.1, border=0.1, command=find_password, background = BACKGROUND)
search_button.grid(column = 2, row = 1, columnspan=2, sticky="ew")

window.mainloop()