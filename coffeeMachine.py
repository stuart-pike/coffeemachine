MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
            "coffee": 18,
        },
        "cost": 3.50,
    },
    "latte": {
        "ingredients": {
            "water": 50,
            "milk": 240,
            "coffee": 20,
        },
        "cost": 4.50,
    },
    "cappuccino": {
        "ingredients": {
            "water": 50,
            "milk": 180,
            "coffee": 20,
        },
        "cost": 4.00,
    }
}


resources = {
    "water": 300,
    "milk": 1000,
    "coffee": 300,
}


def printReport():
    for key in resources:
        print(f"{key}: {resources[key]}")
    print(f"money: ${till}")


def checkResources(drink):
    for key in MENU[drink]["ingredients"]:
        if MENU[drink]['ingredients'][key] > resources[key]:
            print(f"Sorry, there is not enough {key}")
            return False
    return True
    

def coinProcess(drink, payment):
    if MENU[drink]['cost'] < payment:
        change = payment - MENU[drink]['cost']
        print(f"Here is your ${'%.2f' % change} in change")
        print(f"Here is your {drink} ☕. Enjoy")
        # deduct resources to make the drink
        for key in MENU[drink]["ingredients"]:
            resources[key] -= MENU[drink]['ingredients'][key]
        return MENU[drink]['cost']
    else:
        print("Sorry, That's not enough money. Money refunded")
        return False

    
till = 0
in_opperation = True

while in_opperation:
    selection = input(" Which drink would you like? (espresso/cappuccino/latte): ")
    if selection == "off":
        print("Shutting coffee machine down")
        in_opperation = False
    elif selection == "report":
        printReport()
    elif selection in MENU:
        if checkResources(selection):
                print("Please insert coins.")

                quarter = float(input("How many quarters: "))
                dimes = float(input("How many dimes: "))
                nickles = float(input("How many nickles: "))
                pennies = float(input("How many pennies: "))
                sumCoins = 0.25*quarter + 0.1*dimes + 0.05*nickles + 0.01*pennies

                till += (coinProcess(selection, sumCoins))
    


    
