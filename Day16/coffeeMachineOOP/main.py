from typing import Type
from money_machine import MoneyMachine
from menu import Menu
from coffee_maker import CoffeeMaker
import time

coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()


is_on = True


while is_on:
    options = menu.get_items()
    choice = input(f"Want do you want to have? :{options}: ").lower()
    if choice == 'off':
        print("Closing Current Session...")
        time.sleep(2)
        print("Coffee Machine is switched off.")
        is_on = False

    elif choice == 'report':
        coffee_maker.report()
        money_machine.report()

    else:
        drink = menu.find_drink(choice)
        if drink != None:
            if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):

                time.sleep(3)
                coffee_maker.make_coffee(drink)
