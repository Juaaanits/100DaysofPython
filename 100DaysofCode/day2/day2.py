print("Welcome to the tip calculator!")
total = float(input("What is the total bill amount? \n$: "))
percent = float(input("How much tip would you like to give? \nPercent: "))
num = float(input("How many people to split the bill? \nPeople: "))

tip = total * percent * 0.01
print(tip)
amount = (total+tip) / num
print(amount)

print(f"Each person should pay: ${amount}")

'''
Concepts I learned:

-Application of Basic Mathematics in Programming
-Debugging
'''




