from art import logo
import os

auction_info = []

def intro():
    print(logo)
    print("Welcome to the private bidding auction")

def get_bidder_info():
    """Function to get bidder's name, bid amount, and if there are other bidders."""
    name = input("What is your name? ")
    bid_amount = 0.0
    while auction == True:
        try:
            bid_amount = float(input("What is your bid amount? $"))
            if bid_amount < 0:
                print("Bid amount cannot be negative. Please enter a valid amount.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a numeric value for the bid amount.")
    return name, bid_amount

def add_bidder(name, bid_amount):
    """Function to add bidder's name and bid amount to the auction info."""
    auction_info.append({"name": name, "bid_amount": bid_amount})

def find_winner(bids):
    """Function to find the highest bidder."""
    highest_bid = 0.0
    winner = ""
    for bidder in bids:
        if bidder["bid_amount"] > highest_bid:
            highest_bid = bidder["bid_amount"]
            winner = bidder["name"]
    return winner, highest_bid

if __name__ == "__main__":
    auction = True
    while auction:
        intro()
        while auction:
            name, bid_amount = get_bidder_info()
            add_bidder(name, bid_amount)

            while True:
                others = input("Are there any other bidders? Type 'yes' or 'no': ").lower()
                if others in ['yes', 'no']:
                    break
                else:
                    print("Invalid input. Please enter 'yes' or 'no'.")
            
            if others == 'no':
                auction = False
                os.system("cls")
                winner, amount = find_winner(auction_info)
                print(f"The winner is {winner} with a bid of ${amount}.")
                print("Thank you for participating in the auction!")
            else:
                os.system("cls")
                print("Next bidder, please!")






   