from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker = CoffeeMaker()
menu = Menu()
cashier = MoneyMachine()
drinks = menu.get_items()

continue_serving = True
while continue_serving:
    choice = input(f"What would you like? ({drinks}): ").lower()
    if choice == "off":
        continue_serving = False
    elif choice == "report":
        coffee_maker.report()
        cashier.report()
    else:
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink) and cashier.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)