from menu import menuItem, Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

espresso = menuItem("espresso", 50, 0, 18, 1.5)
latte = menuItem("latte", 200, 150, 24, 2.5)
cappuccino = menuItem("cappuccino", 250, 100, 24, 3.0)

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

on = True
while on:
    flavor_choice = input("What would you like? (espresso/latte/cappuccino): ")
    if flavor_choice == "off":
        print("Turning off. ")
        on = False
    elif flavor_choice == "report":
        coffee_maker.report()
        money_machine.report()
        continue
    else:
        coffee_choice = menu.get_item(flavor_choice)
        if coffee_maker.is_resource_sufficient(coffee_choice) and money_machine.make_payment(coffee_choice.cost):
            coffee_maker.make_coffee(coffee_choice)
    
