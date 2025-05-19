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

def make_coffee(order):
    global resources
    res = {key: resources[key] - MENU[order]["ingredients"].get(key, 0) + MENU[order].get(key, 0)
           for key in resources.keys()}
    for k in resources:
        if resources[k] < MENU[order]["ingredients"].get(k, 0):
            print(f"Sorry there is not enough {k}")
            res = resources
            return False
        else:
            resources = res
            return True
    return None


def record():
    for item in resources:
        if item == "coffee":
            print(f"{item.title()}: {resources[item]}g")
        elif item == "cost":
            print(f"Money: ${resources[item]}")
        else:
            print(f"{item.title()}: {resources[item]}ml")

def transaction(order):
    # quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01
    print("Please insert coins.")
    price = MENU[order]["cost"]
    quarters = 0.25
    dimes = 0.10
    nickles = 0.05
    pennies = 0.01
    try:
        quarter = float(input("how many quarters?: "))
        dime = float(input("how many dimes?: "))
        nickle = float(input("how many nickles?: "))
        pennie = float(input("how many pennies?: "))
    except Exception:
        print("insert numerical")
    bill = (quarter * quarters) + (dime * dimes) + (nickle * nickles) + (pennie * pennies)
    if bill < price:
        print("Sorry that's not enough money. Money refunded.")
        return False
    else:
        result = round(bill - price, 2)
        print(f"Here is ${result} dollars in change.")
        return True

def check_coffee(coffe, coin):
    global resources
    if coffe and coin == True:
        print(f"Here is your {service} ☕. Enjoy!")
    else:
        res = {key: resources[key] + MENU[service]["ingredients"].get(key, 0) - MENU[service].get(key, 0)
               for key in resources.keys()}
        resources = res
coffee = True
resources["cost"] = 0
while coffee:
    try:
        service = input("What would you like? (espresso/latte/cappuccino): ").lower()
    except Exception:
        print("please choose menu or 'report' or 'off' to turn off the machine")
    if service == "espresso":
        if make_coffee(service):
            check_coffee(True, transaction(service))
        else:
            continue
    elif service == "latte":
        if make_coffee(service):
            check_coffee(True, transaction(service))
        else:
            continue
    elif service == "cappuccino":
        if make_coffee(service):
            check_coffee(True, transaction(service))
        else:
            continue
    elif service == "report":
        record()
    elif service == "off":
        break
