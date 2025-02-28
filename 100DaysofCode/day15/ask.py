import sys

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

money = {
    "value": 0,
}

def printReport():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${money['value']:.2f}")

def checkResources(flavor_choice):
    enough = True
    if MENU[flavor_choice]['ingredients']['water'] > resources['water']:
        print(f"There is no enough water for a {flavor_choice}.")
        enough = False
    if MENU[flavor_choice]['ingredients']['coffee'] > resources['coffee']:
        print(f"There is no enough coffee for a {flavor_choice}.")
        enough = False   
    if flavor_choice != "espresso":
        if MENU[flavor_choice]['ingredients']['milk'] > resources['milk']:
            print(f"There is no enough milk for a {flavor_choice}.")
            enough = False
    return enough
    

def getUserCoins():
    try:
        quarters = int(input("How many quarters?: "))
        dimes = int(input("How many dimes?: "))
        nickels = int(input("How many nickels?: "))
        pennies = int(input("How many pennies?: "))
        return quarters, dimes, nickels, pennies
    except ValueError:
        print("Invalid input. Please enter numbers only.")
        return getUserCoins()  # Recursively ask for input again
    
    

def processCoins(quarters, dimes, nickels, pennies):
    total =  (quarters * 0.25) + (dimes * 0.10) + (nickels * 0.05) + (pennies * 0.01)
    return total


def deductResources(flavor_choice):
    for ingredient in MENU[flavor_choice]['ingredients']:
        if resources[ingredient] - MENU[flavor_choice]['ingredients'][ingredient] >= 0:
            resources[ingredient] -= MENU[flavor_choice]['ingredients'][ingredient]
        else:
            print(f"Sorry, there is not enough {ingredient}.")
            return False
    return True

def coffeeMachine():
    on = True
    while on:
        flavor_choice = input("What would you like? (espresso/latte/cappuccino): ")
        if flavor_choice == "off":
            print("Turning off. ")
            on = False
        elif flavor_choice == "report":
            printReport()
            continue
        elif flavor_choice in MENU:
            if(checkResources(flavor_choice)):
                print("Please insert coins.")
                quarters, dimes, nickels, pennies = getUserCoins()
                total_inserted = processCoins(quarters, dimes, nickels, pennies)
                
                if total_inserted >= MENU[flavor_choice]['cost']:
                    if deductResources(flavor_choice):
                        money['value'] += MENU[flavor_choice]['cost']
                        change = round(total_inserted - MENU[flavor_choice]['cost'], 2)
                        print(f"Here is your {flavor_choice} ☕. Have a good one!")
                        if change > 0:
                            print(f"Here is your change: ${change:.2f}")
                    else:
                        print(f"Not enough resources. ${total_inserted:.2f} refunded.")
                else:
                    print(f"Not enough money, ${total_inserted:.2f} refunded.")
        else:
            print("Invalid choice. Please select a valid drink.")    

try:
    coffeeMachine()
except KeyboardInterrupt:
    print("\nMachine turned off. Goodbye!")
    sys.exit(0)






    
