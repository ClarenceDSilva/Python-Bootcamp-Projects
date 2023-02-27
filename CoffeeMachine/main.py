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

money = 0


def print_report(money):
    """Prints a report of the resources as well as the money earned"""
    print(f"Water: {resources['water']} ml")
    print(f"Milk: {resources['milk']} ml")
    print(f"Coffee: {resources['coffee']} g")
    print(f"Money: ${format(money, '.2f')}")


def insert_coins(drink_cost):
    """Calculates the change and returns it back to the user"""
    print("\nPlease insert coins")
    quarters = float(input("How many quarters?: "))
    dimes = float(input("How many dimes?: "))
    nickles = float(input("How many nickles?: "))
    pennies = float(input("How many pennies?: "))

    paid_amount = quarters * 0.25 + dimes * 0.1 + nickles * 0.05 + pennies * 0.01
    if paid_amount < drink_cost:
        return -1
    else:
        return format(paid_amount - drink_cost, '.2f')


def check_machine_resources(drink):
    """Checks if there are sufficient ingredients to make the drink"""
    if drink == "espresso":
        return MENU[drink]["ingredients"]["water"] <= resources["water"] and MENU[drink]["ingredients"]["coffee"] <= \
            resources["coffee"]
    return MENU[drink]["ingredients"]["water"] <= resources["water"] and MENU[drink]["ingredients"]["coffee"] <= \
        resources["coffee"] and MENU[drink]["ingredients"]["milk"] <= resources["milk"]


def update_resources(drink):
    """Updates the resources in the machine after the drink is served"""
    resources["water"] -= MENU[drink]["ingredients"]["water"]
    resources["coffee"] -= MENU[drink]["ingredients"]["coffee"]

    if "milk" in MENU[drink]["ingredients"]:
        resources["milk"] -= MENU[drink]["ingredients"]["milk"]


def coffee_machine(money):
    choice = input("What would you like? (Choose options from Espresso, Latte, Cappuccino): ").lower()
    if choice == "off":
        return None
    if choice == "report":
        print_report(money)
        coffee_machine(money)
    if not check_machine_resources(choice):
        print("Sorry, no sufficient resources to make your drink\n")
        coffee_machine(money)

    drink_cost = float(MENU[choice]["cost"])
    change = insert_coins(drink_cost)
    if change == -1:
        print("Sorry, that's not enough money. Your money has been refunded")
        coffee_machine(money)
    else:
        money += drink_cost
        update_resources(choice)
        print(f"Here is ${change} in change")
        print(f"Here is your {choice} Enjoy!")
        coffee_machine(money)


# Start the machine
coffee_machine(money)
