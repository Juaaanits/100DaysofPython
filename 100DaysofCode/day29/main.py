from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
from PIL import Image, ImageTk
import json

def find_password():
    website = website_entry.get()
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showerror(title="Error", message="No Data File Found")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showerror(title="Error", message=f"No details for the website {website} exists.")

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
               'u', 'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8,10))]
    password_symbols = [choice(numbers) for _ in range(randint(2, 4))]
    password_numbers = [choice(symbols) for _ in range(randint(2, 4))]

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
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if len(password) == 0 or len(email) == 0 or len(website) == 0:
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

#Setting Up the GUI  
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg='DarkGoldenrod1')

'''
canvas = Canvas(window, width=200, height=200)
photo = PhotoImage(file='logo.png')  
canvas.create_image(100, 100,image=photo)
canvas.grid(column=1, row=0)
'''
canvas = Canvas(window, width=200, height=200, bg='DarkGoldenrod1', highlightthickness=0)
img = Image.open("C:/Users/Juanito/OneDrive/Desktop/Python Projects/100DaysofPython/100DaysofCode/day29/logo.png")
photo = ImageTk.PhotoImage(img)
canvas.create_image(100, 100, image=photo, anchor=CENTER)
canvas.photo = photo  #Prevent garbage collection
canvas.grid(column=1, row=0)


website_label = Label(text="Website:", bg='DarkGoldenrod1')
website_label.grid(column=0, row=1)
email_label = Label(text="Email/Username:", bg='DarkGoldenrod1')
email_label.grid(column=0, row=2)
password_label = Label(text="Password:", bg='DarkGoldenrod1')
password_label.grid(column=0, row=3)

website_entry = Entry()
website_entry.grid(column=1, row=1)
website_entry.focus()
email_entry = Entry()
email_entry.grid(column=1, row=2)    
email_entry.insert(0, "phillip@email.com")
password_entry = Entry()
password_entry.grid(column=1, row=3)

generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(column=2, row=3)
add_button = Button(text="Add", command=save)
add_button.grid(column=1, row=6)
search_button = Button(text="Search Website", command=find_password, bg='steel blue', fg='white')
search_button.grid(row=1, column=2)
clear_button = Button(text="Clear Info", command=clear_info)
clear_button.grid(row=2, column=2)

window.mainloop()


