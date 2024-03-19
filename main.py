from tkinter import *

# Functions
def create_text_file():
    with open("password_manager.txt", "a") as f, open("password_manager_backup.txt", "a") as file:
        f.writelines(f"{website_entry.get()} | {email_entry.get()} | {password_entry.get()}\n")
        file.writelines(f"{website_entry.get()} | {email_entry.get()} | {password_entry.get()}\n")
        website_entry.delete(0, END)
        password_entry.delete(0, END)

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

# Window
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)
window.resizable(False, False)

# Canvas
lock_png = PhotoImage(file = "logo.png")
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
password_button = Button(text = "Generate Password", border=0.45, width = 14)
password_button.grid(column = 2, row = 3)

add_button = Button(text = "Add", width=30, borderwidth=1, border=0.45, command=create_text_file)
add_button.grid(column = 1, row = 4, columnspan=2, sticky="ew")

window.mainloop()