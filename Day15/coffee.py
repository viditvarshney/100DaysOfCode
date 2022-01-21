import time

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 150.75,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 175.85,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 300.75,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


# def UpdateResources(choosen_drink, Resource):
#     ref = {
#         "espresso": {
#             "water": 50,
#             "milk": 0,
#             "coffee": 18,
#             "money": 1.5
#         },
#         "latte": {
#             "water": 200,
#             "milk": 150,
#             "coffee": 24,
#             "money": 2.5
#         },
#         "cappucinno": {
#             "water": 250,
#             "milk": 100,
#             "coffee": 24,
#             "money": 3.0
#         },
#     }

#     Resource["water"] -= ref[choosen_drink]["water"]
#     Resource["milk"] -= ref[choosen_drink]["milk"]
#     Resource['coffee'] -= ref[choosen_drink]["coffee"]
#     Resource['money'] += ref[choosen_drink]["money"]


profit = 0


# Is the amount received is suuficient for the choosen drink

def transaction_success(tot_amount, drink_cost):
    """Returns TRUE if the transaction is successful otherwise False."""
    # print(drink_cost)  # for testing

    change = round(tot_amount - drink_cost, 2)
    if (tot_amount < drink_cost):
        print(
            f"Amount paid is less. Money Refunded...: {round(tot_amount,2)}")
        return False

    else:
        if(tot_amount > drink_cost):
            print(
                f"Here is your change: {change}.\n")
            global profit
            profit += drink_cost
        print("Your Transaction is successful.\n")
        return True


def making_coffee(drink_name, drink_ingredients):
    """Update the Resources inventory."""
    # print(drink_ingredients)  # Testing
    for item in drink_ingredients:
        resources[item] -= drink_ingredients[item]
    print("Machine took the Ingredients...")
    time.sleep(2)
    print(
        f"Your {drink_name} is on the way. ")
    time.sleep(2)
    print("Take your Drink, ENJOY!\n")
    time.sleep(2)
    print("Next Customer.\n")
    time.sleep(2)


is_on = True
drink_available = ['espresso', 'latte', 'cappuccino', 'off', 'report']

while is_on:

    drink_u_wnt = input(
        "Want do you want to have? : (Espresso / Latte / Cappuccino: ").lower()
    if drink_u_wnt in drink_available:

        if drink_u_wnt == 'off':

            print("Coffee Machine is switched off.")
            is_on = False

        elif drink_u_wnt == 'report':
            print(f"Water: {resources['water']} ml")
            print(f"Milk: {resources['milk']} ml")
            print(f"Coffee: {resources['coffee']} g")
            print(f"Money: ₹ {profit}")

        else:
            print("Insert the amount\n")
            total_amount_received = int(input("How much Rupees: "))
            total_amount_received += int(input("How much Paisa: "))/100

            print(f"Total amount received: {total_amount_received}")
            print("Validating Your Transaction...\n")
            time.sleep(3)

            drink = MENU[drink_u_wnt]

            if transaction_success(total_amount_received, drink["cost"]):
                making_coffee(drink_u_wnt, drink["ingredients"])
    else:
        print("\n")
        print("Invalid Drink Name Entered.\n")
