print("Welcome to the Tip Calculator!")
cost = input("What was the total bill? $")
tip = input("How much tip would you like to give? 10, 12, or 15?")
people = input("How many people to split the bill?")
tip_percentage = int(tip) / 100
result = round(float(cost) * (tip_percentage + 1) / int(people), 2)
print(f"Each person should pay: ${result}")