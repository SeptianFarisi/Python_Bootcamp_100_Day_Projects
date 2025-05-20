from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
espresso = MenuItem("espresso", 50, 0, 18, 1.5).name
latte = MenuItem("latte", 200, 150, 24, 2.5).name
cappuccino = MenuItem("cappuccino", 250, 100, 24, 3.0).name
coffe = CoffeeMaker()
money_machine = MoneyMachine()

def maker(order):
    order_ingredients = menu.find_drink(order)
    order_cost = menu.find_drink(order).cost
    if coffe.is_resource_sufficient(order_ingredients) and money_machine.make_payment(order_cost):
        coffe.make_coffee(order_ingredients)

def report():
    coffe.report()
    money_machine.report()

coffee_machine = True

while coffee_machine:
    order = input(f"What would you like? {menu.get_items()}: ").lower()
    if order == "espresso":
        maker(order)
    elif order == "latte":
        maker(order)
    elif order == "cappuccino":
        maker(order)
    elif order == "off":
        coffee_machine = False
    elif order == "report":
        report()