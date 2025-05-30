from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json

def find_password():
    website = website_entry.get()
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
            search_email = data[website]['email']
            search_password = data[website]['password']
            messagebox.showinfo(title=website.title(), message=f"Email: {search_email}\nPassword: {search_password}")
    except FileNotFoundError:
        messagebox.showerror(title="Error", message="No Data File Found")
    except KeyError:
        messagebox.showerror(title="Error", message="No details for the website exists")
        
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
               'u', 'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8,10))]
    password_symbols += [choice(numbers) for _ in range(randint(2, 4))]
    password_numbers += [choice(symbols) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)
    
    password = ''.join(password_list)
    password_entry.insert(0, password)  # Insert the password into the entry field
    pyperclip.copy(password)  # Copy the password to clipboard

def clear_info():
    website_entry.delete(0, END)
    password_entry.delete(0, END)

def save():
    website = website_entry.get()
    email_username = email_username_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if len(password) == 0 or len(email_username) == 0 or len(website) == 0:
        messagebox.showwarning(title="Empty fields", message="Please don't leave any empty fields")
    else:
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            data.update(new_data)
            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)

# Part 1: Setting Up the GUI
window = Tk()
window.title("Password Manager")
window.config(padx=25, pady=25)

canvas = Canvas(window, width=200, height=200)
photo = PhotoImage(file='logo.png')  # Ensure you have a logo.png file in the same directory
canvas.create_image(100, 100,image=photo)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:")
website_label.grid(column=0, row=1)
email_username_label = Label(text="Email/Username:")
email_username_label.grid(column=0, row=2)
password_label = Label(text="Password:", width=21)
password_label.grid(column=0, row=3)

website_entry = Entry(width=35)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()
email_entry = Entry(width=35)
email_entry.grid(column=1, row=2, columnspan=2)    
email_entry.insert(0, "phillip@email.com")
password_entry = Entry(width=22)
password_entry.grid(column=1, row=3)

generate_password_button = Button(text="Generate Password", width=21, command=generate_password)
generate_password_button.grid(column=2, row=3, columnspan=2)
add_button = Button(text="Add", width=36, command=save)
add_button.grid(column=1, row=4, columnspan=2)
search_button = Button(text="Search Website", command=find_password)
search_button.grid(row=1, column=2)
clear_button = Button(text="Clear Info", command=clear_info)
clear_button.grid(row=2, column=2)

window.mainloop()


