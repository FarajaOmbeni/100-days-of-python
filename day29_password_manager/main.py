from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    #Password Generator Project
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = []

    password_list = [choice(letters) for _ in range(randint(8, 10))]
    password_list += [choice(numbers) for _ in range(randint(2, 4))]
    password_list += [choice(symbols) for _ in range(randint(2, 4))]

    shuffle(password_list)

    password = "".join(password_list)

    password_input.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_to_file():
    inserted_website = website_input.get()
    inserted_email = email_input.get()
    inserted_password = password_input.get()

    if (len(inserted_email) == 0):
        messagebox.showinfo(title="Error", message="The email field is required")
    elif (len(inserted_website) == 0):
        messagebox.showinfo(title="Error", message="The webiste field is required")
    elif (len(inserted_password) == 0):
        messagebox.showinfo(title="Error", message="The password field is required")
    else:
        is_ok = messagebox.askokcancel(title=inserted_website, message=f"These are the detials entered:\nEmail:{inserted_email}\nPassword:{inserted_password}\nIs it ok to save?")

        if is_ok:
            with open('data.txt', 'a')as file:
                file.writelines(f"{inserted_website} | {inserted_email} | {inserted_password}\n")
            website_input.delete(0, END)
            password_input.delete(0, END)
    

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=1)

#Labels
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

#Entries
website_input = Entry(width=53)
website_input.grid(row=1, column=1, columnspan=2)
website_input.focus()
email_input = Entry(width=53)
email_input.grid(row=2, column=1, columnspan=2)
email_input.insert(0, "ombenifaraja@gmail.com")
password_input = Entry(width=34)
password_input.grid(row=3, column=1)

#Buttons
generate_pw_button = Button(text="Generate Password", width=15, command=generate_password)
generate_pw_button.grid(row=3, column=2)
add_button = Button(text="Add", width=45, command=save_to_file)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()