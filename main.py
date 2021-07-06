import menu
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


obj_menu = Menu()

obj_coffee = CoffeeMaker()

obj_money = MoneyMachine()

machine_on = True

sufficient = True

items = []

while machine_on:

    choice = input(f"\nWhat would you like to have ({obj_menu.get_items()}):\t").lower()

    if choice == "report":
        obj_coffee.report()
        obj_money.report()

    elif choice == "off":

        machine_on = False

    else:

        is_choice_correct = obj_menu.find_drink(choice)

        if is_choice_correct.name == choice:

            if obj_coffee.is_resource_sufficient(is_choice_correct) and obj_money.make_payment(is_choice_correct.cost):

                obj_coffee.make_coffee(is_choice_correct)

            else:

                machine_on = False

        else:

            machine_on = False
