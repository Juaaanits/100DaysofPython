class CoffeeMaker:
    def __init__(self):
        self.resources = {
            "water": 300,
            "milk": 200,
            "coffee": 100,
        }

    def report(self):
        "Prints the current resource values."
        print(f"Water: {self.resources['water']}ml")
        print(f"Milk: {self.resources['milk']}ml")
        print(f"Coffee: {self.resources['coffee']}g")

    def is_resource_sufficient(self, drink):
        "Returns True when the drink can be made, False if ingredients are insufficient."
        enough = True
        for item in drink.ingredients:
            if drink.ingredients[item] > self.resources[item]:
                print(f"There is not enough {item}.")
                enough = False
        return enough
    
    def make_coffee(self, order):
        for item in order.ingredients:
            if order.ingredients[item] - self.resources[item] >= 0:
                order.ingredients[item] -= self.resources[item]
            else:
                print(f"Sorry there is not enough {item}.")
                return False
        print(f"Here is your {order.name}. Enjoy!")
