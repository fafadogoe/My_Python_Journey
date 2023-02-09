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


def report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${resources['monies']}")


# TODO. 5. Adding of coins
def add_coins():
    print("Please insert coins")
    q = float(input("How many quaters?: "))
    d = float(input("How many dimes?: "))
    n = float(input("How many nickels?: "))
    p = float(input("How many pennies?: "))
    c1 = 0.25 * q
    c2 = 0.10 * d
    c3 = 0.05 * n
    c4 = 0.01 * p
    total_add = c1 + c2 + c3 + c4
    return round(total_add)

resources["monies"] = 0
resources["money"] = 0

loop = True
while loop is True:
    # TODO: 1.  Prompt user
    prompt = input("What would you like? (espresso/latte/cappuccino): ").lower()

    # TODO: 2. Turn off the coffee machine
    if prompt == "off":
        loop = False

    # TODO: 3. print report
    elif prompt == "report":
        report()

    # TODO. 4. latte input
    elif prompt == "latte":
        if resources["money"] == 0:
            total_added_coins = add_coins()
            resources["money"] += total_added_coins
            resources["monies"] += MENU["latte"]["cost"]
        latte1 = resources["money"] - MENU["latte"]["cost"]
        latte2 = resources["water"] - MENU["latte"]["ingredients"]["water"]
        latte3 = resources["milk"] - MENU["latte"]["ingredients"]["milk"]
        latte4 = resources["coffee"] - MENU["latte"]["ingredients"]["coffee"]

        if latte1 < 0 or latte2 < 0 or latte3 < 0 or latte4 < 0:
            if latte2 < 0:
                print("Sorry there is not enough water")
            elif latte3 < 0:
                print("Sorry there is not enough milk")
            elif latte4 < 0:
                print("Sorry there is not enough coffee")
            elif latte1 < 0:
                print("Sorry that's not enough money")
                print("Money refunded")
        else:
            resources["money"] -= MENU["latte"]["cost"]
            resources["water"] -= MENU["latte"]["ingredients"]["water"]
            resources["milk"] -= MENU["latte"]["ingredients"]["milk"]
            resources["coffee"] -= MENU["latte"]["ingredients"]["coffee"]
            print(f"Here is ${round(latte1,2)} in change")
            print("Here is your latte☕. Enjoy!")

    # TODO. 6. Espresso Input
    elif prompt == "espresso":
        if resources["money"] == 0:
            total_added_coins = add_coins()
            resources["money"] += total_added_coins
            resources["monies"] += MENU['espresso']["cost"]
        espresso1 = resources["money"] - MENU["espresso"]["cost"]
        espresso2 = resources["water"] - MENU["espresso"]["ingredients"]["water"]
        espresso3 = resources["coffee"] - MENU["espresso"]["ingredients"]["coffee"]

        if espresso1 < 0 or espresso2 < 0 or espresso3 < 0:
            if espresso2 < 0:
                print("Sorry there is not enough water")
            elif espresso3 < 0:
                print("Sorry there is not enough coffee")
            elif espresso1 < 0:
                print("Sorry that's not enough money")
                print("Money refunded")
        else:
            resources["money"] -= MENU["espresso"]["cost"]
            resources["water"] -= MENU["espresso"]["ingredients"]["water"]
            resources["coffee"] -= MENU["espresso"]["ingredients"]["coffee"]
            print(f"Here is ${round(espresso1,2)} in change")
            print("Here is your latte☕. Enjoy!")

    # TODO. 7. Cappuccino Input
    elif prompt == "cappuccino":
        if resources["money"] == 0:
            total_added_coins = add_coins()
            resources["money"] += total_added_coins
            resources["monies"] += MENU["espresso"]["cost"]
        cappuccino1 = resources["money"] - MENU["cappuccino"]["cost"]
        cappuccino2 = resources["water"] - MENU["cappuccino"]["ingredients"]["water"]
        cappuccino3 = resources["milk"] - MENU["cappuccino"]["ingredients"]["milk"]
        cappuccino4 = resources["coffee"] - MENU["cappuccino"]["ingredients"]["coffee"]

        if cappuccino1 < 0 or cappuccino2 < 0 or cappuccino3 < 0 or cappuccino4 < 0:
            if cappuccino2 < 0:
                print("Sorry there is not enough water")
            elif cappuccino3 < 0:
                print("Sorry there is not enough milk")
            elif cappuccino4 < 0:
                print("Sorry there is not enough coffee")
            elif cappuccino1 < 0:
                print("Sorry that's not enough money")
                print("Money refunded")
        else:
            resources["money"] -= MENU["cappuccino"]["cost"]
            resources["water"] -= MENU["cappuccino"]["ingredients"]["water"]
            resources["milk"] -= MENU["cappuccino"]["ingredients"]["milk"]
            resources["coffee"] -= MENU["cappuccino"]["ingredients"]["coffee"]
            print(f"Here is ${round(cappuccino1,2)} in change")
            print("Here is your cappuccino☕. Enjoy!")