from tkinter import *
from tkinter import messagebox
from random import choice, shuffle, randint
import pyperclip

FONT_NAME = "Courier"


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_field.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_field.get()
    email = email_field.get()
    password = password_field.get()

    if not website or not email or not password:
        messagebox.showinfo(title="Empty Fields", message="One or more fields are empty, kindly check the "
                                                          "inputs entered")
    else:
        is_ok = messagebox.askokcancel(title="Confirm Details",
                                       message=f"These are the details entered: \nEmail: {email}"
                                               f"\nPassword: {password} for {website}\n\nIs it "
                                               f"ok to save?")
        if is_ok:
            file = open("passwords.txt", "a")
            file.write(f"{website} | {email} | {password} \n")
            file.close()

            # Clearing the contents of the entry fields
            website_field.delete(0, END)
            email_field.delete(0, END)
            password_field.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200, highlightthickness=0)
logo_img = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# Labels
website_label = Label(text='Website:')
website_label.grid(row=1, column=0)

email_label = Label(text='Email/Username:')
email_label.grid(row=2, column=0)

password_label = Label(text='Password:')
password_label.grid(row=3, column=0)

# Buttons
generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(row=3, column=2)

add_button = Button(text="Add", width=35, command=save)
add_button.grid(row=4, column=1)

# Entry
website_field = Entry(width=35)
website_field.grid(row=1, column=1)
website_field.focus()

email_field = Entry(width=35)
email_field.grid(row=2, column=1)

password_field = Entry(width=35)
password_field.grid(row=3, column=1)

window.mainloop()
