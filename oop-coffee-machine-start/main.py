from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
menu_item = MenuItem()
coffe_maker = CoffeeMaker()

is_on = True
while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino):")
    if choice == "off":
        is_on = False

    elif  choice == "report":
        print(coffe_maker.report("report"))

