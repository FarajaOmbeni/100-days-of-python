MENU = {
    'espresso':{
        'ingredients': {
            'water': 50,
            'coffee': 18,
        },
        'cost': 1.5,
    },
    'latte':{
        'ingredients': {
            'water': 200,
            'milk': 150,
            'coffee': 24,
        },
        'cost': 2.5,
    },
    'cappuccino':{
        'ingredients': {
            'water': 250,
            'milk': 100,
            'coffee': 24,
        },
        'cost': 3.0,
    },
}

resources = {
    'water': 300,
    'milk': 200,
    'coffee': 100,
}

water = resources['water']
milk = resources['milk']
coffee = resources['coffee']
money = 0

def process_coins():
    '''Calculates and returns the actual value of the coins inserted'''
    quarters = int(input("How many quarters? "))
    dimes = int(input("How many dimes? "))
    nickles = int(input("How many nickles? "))
    pennies = int(input("How many pennies? "))

    return float(0.25*quarters + 0.1*dimes + 0.05*nickles + 0.01*pennies)

def check_ingredients(order: str):
    '''Takes in a coffee as argument and returns a report on the ingredient'''
    if water < MENU[order]['ingredients']['water']:
        return "Sorry, there is not enough water"
    elif coffee < MENU[order]['ingredients']['coffee']:
        return "Sorry, there is not enough coffee"
    if order == 'cappuccino' or order == 'latte':
        if milk < MENU[order]['ingredients']['milk']:
            return "Sorry, there is not enough milk"
    return "Please insert coins."

def get_price(order: str):
    '''Takes in a coffee and returns its price'''
    return MENU[order]['cost']

def confirm_transaction(order: str):
    '''Takes in the order and returns if the transaction was successfull'''
    order_water = MENU[order]['ingredients']['water']
    order_coffee = MENU[order]['ingredients']['coffee']

    global water, milk, coffee, money
    print(check_ingredients(order))
    if check_ingredients(order) == "Please insert coins.":
        inserted_amount = process_coins()
        price = get_price(order)
        if inserted_amount < price:
            print("Sorry that's not enough money. Money refunded")
        elif inserted_amount > price or inserted_amount == price:
            water -= order_water
            coffee -= order_coffee
            if order == 'cappuccino' or order == 'latte':
                MENU[order]['ingredients']['milk']
            balance = round(inserted_amount - price, 2)
            money += price
            print(f"Here is ${balance} in change.")
            print(f"Here is your {order}. Enjoy!")

continue_serving = True    
while continue_serving:
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    drinks = []
    for item in MENU:
        drinks.append(item)
    print(drinks)
    if choice == 'report':
        print(f"Water: {water}ml\nMilk: {milk}ml\nCoffee: {coffee}g\nMoney: ${money}")
    elif choice == 'off':
        continue_serving = False
    elif choice not in drinks:
        print("Choose a valid drink.")
    else:
        confirm_transaction(choice)