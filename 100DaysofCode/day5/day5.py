import random

letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 
    'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

characters = [
    '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', 
    ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~'
]


print("Welcome to PyPassword Generator!")

numberOfLetters = int(input("How many letters do you want?: "))
numberOfSymbols = int(input("How many symbols do you want?: "))
numberOfNumbers = int(input("How many numbers do you want?: "))

password = ""


for i in range(0, numberOfLetters):
    randomLetter = random.choice(letters)
    password += randomLetter


for i in range(0, numberOfSymbols):
    randomSymbol = random.choice(characters)
    password += randomSymbol

for i in range(0, numberOfNumbers):
    randomNumber = random.choice(numbers)
    password += randomNumber

shuffledPassword = ''.join(random.sample(password, len(password)))

if len(password) >= 8:
    print("Your password is strong.")

else:
    print("Your password is weak.")

print(f"Your password is: {shuffledPassword}")


print("Invalid input. Please try again.")
exit()
