
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
    "money": 0.0
}

# Process the Coin
quater = 0.25
dimes = 0.1
nickles = 0.05
pennies = 0.01


drink_u_wnt = input(
    "Want do you want to have? : (Espresso / Latte / Cappuccino: ").lower()


#  update resources


def UpdateResources(choosen_drink, Resource):
    ref = {
        "espresso": {
            "water": 50,
            "milk": 0,
            "coffee": 18,
            "money": 1.5
        },
        "latte": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
            "money": 2.5
        },
        "cappucinno": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
            "money": 3.0
        },
    }

    Resource["water"] -= ref[choosen_drink]["water"]
    Resource["milk"] -= ref[choosen_drink]["milk"]
    Resource['coffee'] -= ref[choosen_drink]["coffee"]
    Resource['money'] += ref[choosen_drink]["money"]


# Is the amount received is suuficient for the choosen drink


def transaction(tot_amount, Menu, choosen_drink, resource):
    print("choosen drink cost: ", Menu[choosen_drink]['cost'])  # for testing
    if (tot_amount < Menu[choosen_drink]['cost']):
        print(
            f"Amount paid is less. Money Refunded...: {round(tot_amount,2)}")

    elif(tot_amount > Menu[choosen_drink]['cost']):
        print(
            f"Here is your change: {round(tot_amount - Menu[choosen_drink]['cost'], 2)}.\n")
        print(
            f"Your transaction is successful, Your {choosen_drink} is on the way. ")
        UpdateResources(choosen_drink, resource)

    else:
        print(
            f"Your transaction is successful, Your {choosen_drink} is on the way. ")


if drink_u_wnt == 'off':

    print("Coffee Machine is switched off.")

elif drink_u_wnt == 'report':
    print(resources)


else:

    print("Enter the amount\n")
    in_quater = float(input("Quaters: "))
    in_dimes = float(input("Dimes: "))
    in_nickles = float(input("Nickles: "))
    in_pennies = float(input("Pennies: "))
    total_amount_received = (in_quater*quater) + (in_dimes * dimes) + \
        (in_nickles*nickles) + (in_pennies*pennies)
    print(f"Total amount received: {total_amount_received}")

    transaction(total_amount_received, MENU, drink_u_wnt, resources)
