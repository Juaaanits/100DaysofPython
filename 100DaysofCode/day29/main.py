'''

Build Your Own Password Manager: Step-by-Step Instructions
This activity challenges you to recreate the Python password manager application from scratch, based on a set of instructions. Your goal is to implement all the core functionalities and the graphical user interface (GUI) without referring to the original code you previously sent.

Part 1: Setting Up the GUI (Tkinter Basics)
Create the Main Window:

Start by importing everything from tkinter.

Create the main Tk window object and assign it to a variable (e.g., window).

Set the title of the window to "Password Manager".

Configure the window to have padding of 25 pixels on all sides (both padx and pady).

Add the Logo Canvas:

Create a Canvas widget with a width of 200 and a height of 200.

Load an image file named logo.png using PhotoImage. (Note: You'll need a logo.png file in the same directory for this to work).

Place the image on the canvas at coordinates (100, 100).

Position the canvas in the GUI using the grid layout manager: column=1, row=0.

Create Labels:

Create three Label widgets with the text: "Website:", "Email/Username:", and "Password:".

For the "Password:" label, set its width to 21.

Position these labels using grid:

"Website:": column=0, row=1

"Email/Username:": column=0, row=2

"Password:": column=0, row=3

Create Entry Fields:

Create three Entry widgets for user input:

One for "Website" with a width of 35.

One for "Email/Username" with a width of 35.

One for "Password" with a width of 22.

Position these entry fields using grid:

Website entry: column=1, row=1, columnspan=2

Email/Username entry: column=1, row=2, columnspan=2

Password entry: column=1, row=3

Set the initial keyboard focus to the website entry field.

Pre-fill the email/username entry field with the text "phillip@email.com".

Add Buttons:

Create two Button widgets:

One with the text "Generate Password" and a width of 21.

One with the text "Add" and a width of 36.

Position these buttons using grid:

"Generate Password" button: column=2, row=3, columnspan=2

"Add" button: column=1, row=4, columnspan=2

Start the GUI Event Loop:

Add the line that starts the Tkinter event loop, keeping the window open and responsive.

Part 2: Implementing Password Generation Functionality
Define generate_password() Function:

Create a function named generate_password().

Inside this function, define three lists:

letters: Containing all lowercase and uppercase English alphabet characters.

numbers: Containing digits '0' through '9'.

symbols: Containing ['!', '#', '$', '%', '&', '(', ')', '*', '+'].

Generate Password Components:

Create an empty list (e.g., password_list).

Append random letters to password_list: choose between 8 and 10 random letters.

Append random symbols to password_list: choose between 2 and 4 random symbols.

Append random numbers to password_list: choose between 2 and 4 random numbers.

Important: Use list comprehensions or loops with random.choice() and random.randint() for this.

Shuffle and Join:

Randomly shuffle the password_list to mix the characters.

Join the characters in password_list into a single string to form the final password.

Display and Copy Password:

Clear any existing text in the password_entry field.

Insert the newly generated password into the password_entry field.

Copy the generated password to the system clipboard using the pyperclip library.

Link to Button:

Go back to where you defined the "Generate Password" button in Part 1.

Set its command attribute to generate_password.

Part 3: Implementing Save Functionality
Define save() Function:

Create a function named save().

Inside this function, retrieve the current text from the website_entry, email_username_entry, and password_entry fields.

Input Validation:

Add an if statement to check if either the password or website fields are empty.

If either is empty, display a warning message box with the title "Empty fields" and the message "Please don't leave any empty fields". Use tkinter.messagebox.showwarning().

User Confirmation:

If the fields are not empty, use tkinter.messagebox.askokcancel() to ask the user for confirmation before saving.

Set the title of the confirmation box to the website name.

Set the message to display the entered email and password, asking "Is it OK to save?".

Save to File:

If the user clicks "OK" on the confirmation dialog:

Open a file named data.txt in append mode ("a"). Use a with statement to ensure the file is properly closed.

Write the website, email, and password to the file, separated by " | ", followed by a newline character (\n). The format should be Website | Email | Password\n.

After writing, clear the website_entry and password_entry fields.

Link to Button:

Go back to where you defined the "Add" button in Part 1.

Set its command attribute to save.

Part 4: Imports Review
At the very top of your Python file, ensure you have all the necessary imports:

from tkinter import *

from tkinter import messagebox

from random import choice, randint, shuffle

import pyperclip

Part 5: Running Your Code
Save your Python file (e.g., password_manager.py).

Make sure you have a logo.png image file in the same directory as your Python script.

Run the script from your terminal: python password_manager.py

Good luck!
'''

'''
from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
#import pyperclip
import tkinter as tk
from PIL import Image, ImageTk
'''

from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk


window = tk.Tk()
canvas = tk.Canvas(window, width=200, height=200)
canvas.pack()

image = Image.open("logo.png")
photo = ImageTk.PhotoImage(image)

canvas.create_image(100, 100,image=photo)

window.title("Password Manager")

w = Label(window, text="Password Manager")
w.pack(padx=100, pady=25)

window.mainloop()

'''
window.pack(padx=25, pady=25)

c = Canvas(window, 200, 200)

image = Image.open('logo.png')

photo = ImageTk.PhotoImage(image)

label = tk.label(window, image=photo)
''''''


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
               'u', 'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = [choice(letters) for _ in range(randint)]
    pass
    '''