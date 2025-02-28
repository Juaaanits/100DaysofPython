import random

# Get the user's choice
humanChoice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors \n0/1/2: "))
while humanChoice not in [0, 1, 2]:
    humanChoice = int(input("Invalid Choice. Please try again: "))

# Generate the computer's choice
computerChoice = random.randint(0, 2)

# Function to print the human choice
def human():
    if humanChoice == 0:
        print("You chose: Rock")
        print("""
            _______
        ---'   ____)
            (_____)
            (_____)
            (____)
        ---.__(___)
        """)
    elif humanChoice == 1:
        print("You chose: Paper")
        print("""
            _______
        ---'    ____)____
                ______)
                _______)
                _______)
        ---.__________)
        """)
    elif humanChoice == 2:
        print("You chose: Scissors")
        print("""
            _______
        ---'   ____)____
                ______)
            __________)
            (____)
        ---.__(___)
        """)

# Function to print the computer's choice
def computer():
    if computerChoice == 0:
        print("The computer chose: Rock")
        print("""
            _______
        ---'   ____)
            (_____)
            (_____)
            (____)
        ---.__(___)
        """)
    elif computerChoice == 1:
        print("The computer chose: Paper")
        print("""
            _______
        ---'    ____)____
                ______)
                _______)
                _______)
        ---.__________)
        """)
    elif computerChoice == 2:
        print("The computer chose: Scissors")
        print("""
            _______
        ---'   ____)____
                ______)
            __________)
            (____)
        ---.__(___)
        """)

# Function to compare choices and determine the winner
def comparisonOfChoices():
    human()
    computer()

    if humanChoice == computerChoice:
        print("It's a draw!")
    elif (humanChoice == 0 and computerChoice == 2) or \
         (humanChoice == 1 and computerChoice == 0) or \
         (humanChoice == 2 and computerChoice == 1):
        print("You win!")
    else:
        print("You lose!")

# Compare the choices
comparisonOfChoices()
