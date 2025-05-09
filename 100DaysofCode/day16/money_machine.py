class MoneyMachine:

    CURRENCY = "$"

    COIN_VALUES = {
        "quarters": 0.25,   
        "dimes": 0.1,
        "nickles": 0.05,
        "pennies": 0.01
    }

    def __init__(self):
        self.profit = 0                 
        self.money_received = 0

    # For printing the current profit
    def report(self):
        print(f"Money: {self.CURRENCY}{self.profit}")

    # For processing the coins
    def process_coins(self):
        print("Please insert coins.")
        for coin in self.COIN_VALUES:
            self.money_received += int(input(f"How many {coin}?: ")) * self.COIN_VALUES[coin]
        return self.money_received
    
    def make_payment(self, cost):
        self.process_coins()
        if self.money_received >= cost:
            change = round(self.money_received - cost, 2)
            print(f"Here is {self.CURRENCY}{change} in change.")
            self.profit += cost
            return True
        else:
            print("Sorry that's not enough money. Money refunded.")
            return False


