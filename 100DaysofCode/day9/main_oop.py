from art import logo
import os

def clear_screen():
    """Function to clear the console screen."""
    os.system("cls" if os.name == "nt" else "clear")

class Auction:
    def __init__(self):
        self.auction_info = []
        self.auction = True

    def intro(self):
        print(logo)
        print("Welcome to the private bidding auction")

    def get_bidder_info(self):
        """Function to get bidder's name, bid amount, and if there are other bidders."""
        name = input("What is your name? ")
        bid_amount = 0.0
        while self.auction == True:
            try:
                bid_amount = float(input("What is your bid amount? $"))
                if bid_amount < 0:
                    print("Bid amount cannot be negative. Please enter a valid amount.")
                else:
                    break
            except ValueError:
                print("Invalid input. Please enter a numeric value for the bid amount.")
        return name, bid_amount

    def add_bidder(self, name, bid_amount):
        """Function to add bidder's name and bid amount to the auction info."""
        self.auction_info.append({"name": name, "bid_amount": bid_amount})

    def find_winner(self):
        """Function to find the highest bidder."""
        highest_bid = 0.0
        winner = ""

        if not self.auction_info:
            return "No bidders", 0.0

        for bidder in self.auction_info:
            if bidder["bid_amount"] > highest_bid:
                highest_bid = bidder["bid_amount"]
                winner = bidder["name"]
        return winner, highest_bid
    
    def run_auction(self):
        self.intro()

        while self.auction:
            name, bid_amount = self.get_bidder_info()
            self.add_bidder(name, bid_amount)

            while True:
                others = input("Are there any other bidders? Type 'yes' or 'no': ").lower()
                if others in ['yes', 'no']:
                    break
                else:
                    print("Invalid input. Please enter 'yes' or 'no'.")
            
            if others == 'no':
                auction = False
                os.system("cls")
                winner, amount = self.find_winner()
                print(f"The winner is {winner} with a bid of ${amount}.")
                print("Thank you for participating in the auction!")
            else:
                clear_screen()
                print("Next bidder, please!")

if __name__ == "__main__":
    my_auction = Auction()
    my_auction.run_auction()






   