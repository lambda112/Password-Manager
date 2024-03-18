from tkinter import *
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

lock_png = PhotoImage(file = "logo.png")
canvas = Canvas(height=200, width=200)
lock_image = canvas.create_image(100, 100,image = lock_png)
canvas.grid(column=0,row=0)

window.mainloop()