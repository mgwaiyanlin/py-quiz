MACHINE = {
    "expresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18
        },
        "cost": 1.50
    },
    "latte": {
        "ingredients": {
            "water":200,
            "milk": 150,
            "coffee": 24
        },
        "cost": 2.50
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24
        },
        "cost": 3.00
    }
}

resources = {
    "water": 1000,
    "milk": 500,
    "coffee": 250
}

is_machine_on = 1

print("--- Welcome to Py's Coffee Machine ---")
print('''
READ THE USER MANUAL GUIDE
    # Type the available coffee options you want.
    # Type 'off' to turn off the machine
    # Type 'report' to see the available resources
    # Type 'price' to see the price list of available coffee
''')

def insert_coin(cost):
    print("Please, insert coin here -")
    penny = float(input("How much peeny?: "))
    nickel = float(input("How much nickel?: "))
    dime = float(input("How much dime?: "))
    quarter = float(input("How much quarter?: "))

    addition = penny + nickel + dime + quarter
    if round(addition, 2) < cost:
        print(f"Very sorry to say, {round(addition, 2)} is not enough to make a cup of coffee! 😞")
        return False
    elif round(addition, 2) > cost:
        exchange = round(round(addition, 2) - cost, 2)
        print(f"Here is your exchange: {exchange}")
        return True

def make_expresso():
    required_water = MACHINE["expresso"]["ingredients"]["water"]
    required_coffee = MACHINE["expresso"]["ingredients"]["coffee"]
    expresso_cost = MACHINE["expresso"]["cost"]

    if resources["water"] > required_water and resources["coffee"] > required_coffee:
        money_enough = insert_coin(expresso_cost)
        if money_enough == True:
            resources["water"] -= required_water
            resources["coffee"] -= required_coffee
            print("Here is your EXPRESSO ☕. Enjoy!")
    else:
        print("Not enough resources to make 'Expresso' for you!")

def make_latte():
    required_water = MACHINE["latte"]["ingredients"]["water"]
    required_coffee = MACHINE["latte"]["ingredients"]["coffee"]
    required_milk = MACHINE['latte']['ingredients']['milk']
    expresso_cost = MACHINE["latte"]["cost"]

    if resources["water"] > required_water and resources["coffee"] > required_coffee and resources["milk"] > required_milk:
        money_enough = insert_coin(expresso_cost)
        if money_enough == True:
            resources["water"] -= required_water
            resources["coffee"] -= required_coffee
            resources["milk"] -= required_milk
            print("Here is your LATTE ☕. Enjoy!")
    else:
        print("Not enough resources to make 'Latte' for you!")

def make_cappuccino():
    required_water = MACHINE["cappuccino"]["ingredients"]["water"]
    required_coffee = MACHINE["cappuccino"]["ingredients"]["coffee"]
    required_milk = MACHINE['cappuccino']['ingredients']['milk']
    expresso_cost = MACHINE["cappuccino"]["cost"]

    if resources["water"] > required_water and resources["coffee"] > required_coffee and resources["milk"] > required_milk:
        money_enough = insert_coin(expresso_cost)
        if money_enough == True:
            resources["water"] -= required_water
            resources["coffee"] -= required_coffee
            resources["milk"] -= required_milk
            print("Here is your CAPPUCCINO ☕. Enjoy!")
    else:
        print("Not enough resources to make 'Cappuccino' for you!")

def report():
    print(f'Water: {resources["water"]} ml')
    print(f'Milk: {resources["milk"]} ml')
    print(f'Coffee: {resources["coffee"]} ml')

def price_list():
    print(f'Expresso: ${MACHINE["expresso"]["cost"]}')
    print(f'Latte: ${MACHINE["latte"]["cost"]}')
    print(f'Cappuccino: ${MACHINE["cappuccino"]["cost"]}')

while is_machine_on == 1:
    user_input = input("What would you like? (expresso/latte/cappuccino): ").lower()

    match user_input:
        case "expresso":
            make_expresso()
        case "latte":
            make_latte()
        case "cappuccino":
            make_cappuccino()
        case "report":
            report()
        case "price":
            price_list()
        case "off":
            is_machine_on = 0
        case _:
            print("Your prompt is incorrect!")


print("MACHINE IS OFF!")





