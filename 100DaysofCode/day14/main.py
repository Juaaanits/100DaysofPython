from art import logo, vs
from game_data import data
import random
import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def profile():
    random_index = random.randint(0, 49)
    name = data[random_index]['name']
    follower_count = data[random_index]['follower_count']
    description = data[random_index]['description']
    country = data[random_index]['country']
    compare = f"{name}, a {description}, from {country}."
    return compare, follower_count

def is_guess_correct(guess, followers_a, followers_b):
    if guess == 'a':
        return followers_a >= followers_b
    else:
        return followers_b >= followers_a

def higher_lower():
    profile_a, followers_a = profile()
    profile_b, followers_b = profile()

    while profile_b == profile_a:
        profile_b, followers_b = profile()
    
    score = 0
    correct = True

    while correct:
        clear()
        print(logo)
        if score > 0:
            print(f"Correct! Your current score is: {score}.")
        print(f"Compare A: {profile_a}")
        print(vs)
        print(f"Compare B: {profile_b}")

        guess = input("\nWho do you think has more followers? Type 'a', or 'b': ").lower()
        if guess not in ['a', 'b']:
            print("Invalid input. Please type 'a' or 'b'.")
            continue
        
        
        # Game Logic
        if is_guess_correct(guess, followers_a, followers_b):
            score += 1
            profile_a, followers_a = profile_b, followers_b
            profile_b, followers_b = profile()
        else:
            print(f"\nGame Over! Your final score is {score}.")
            correct = False
    
def main():
    while True:
        higher_lower()
        play_again = input("\nDo you want to play again? Type 'y' or 'n': ")
        if play_again.lower() != 'y':
            print("Thanks for playing! ")
            break

if __name__ == "__main__":
    main()