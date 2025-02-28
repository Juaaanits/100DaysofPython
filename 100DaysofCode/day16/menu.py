class menuItem:
    def __init__(self, name, water, milk, coffee, cost):
        self.name = name
        self.cost = cost
        self.ingredients = {
            "water": water,
            "milk": milk,
            "coffee": coffee
        }

class Menu:
    def __init__(self):
        self.menu = [
            menuItem(name="latte", water=200, milk=150, coffee=24, cost=2.5),
            menuItem(name="cappuccino", water=250, milk=50, coffee=24, cost=3.0),
            menuItem(name="espresso", water=50, milk=0, coffee=18, cost=1.5)
            ]
    
    def get_menu(self):
        choices = ""
        for item in self.menu:
            choices += item.name + " / "
        return choices
    
    def get_item(self, order_name):
        for item in self.menu:
            if item.name == order_name:
                return item
        print("Sorry, that item is not on the menu.")
        return None
            
