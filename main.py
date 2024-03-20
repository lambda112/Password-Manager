from tkinter import *
from tkinter import messagebox # Not a Class
from pyperclip import copy
from password import generate_password
import sys, os

# Functions
def create_text_file():
    if len(website_entry.get()) == 0 or len(password_entry.get()) == 0:
        messagebox.showwarning(title="empty fields", message="Please fill in all the required fields!")

    else:
        is_okay = messagebox.askokcancel(title=website_entry.get()\
                ,message=f"Are these details correct?:\n{email_entry.get()}\
                \n{password_entry.get()}\nSave details?")

        if is_okay:
            with open("password_manager.txt", "a") as f, open("password_manager_backup.txt", "a") as file:
                f.writelines(f"{website_entry.get()} | {email_entry.get()} | {password_entry.get()}\n")
                file.writelines(f"{website_entry.get()} | {email_entry.get()} | {password_entry.get()}\n")

                website_entry.delete(0, END)
                password_entry.delete(0, END)

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
password_button = Button(text = "Generate Password", border=0.45, width = 14, command=create_password)
password_button.grid(column = 2, row = 3)

add_button = Button(text = "Add", width=30, borderwidth=1, border=0.45, command=create_text_file)
add_button.grid(column = 1, row = 4, columnspan=2, sticky="ew")

window.mainloop()