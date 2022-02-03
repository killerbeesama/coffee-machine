from coffee_machine_data import MENU,resources
import os

def check_resources(order_ingredients):
    '''checks if enough resources is available and return True or False'''
    for i in order_ingredients:
        if order_ingredients[i] >= resources[i]:
            print(f"Sorry there is not enough {i}")
            return False
    return True


def update_resources(ordered_ingredients):
    '''Deducts resources'''
    for i in ordered_ingredients:
        resources[i] -= ordered_ingredients[i]


money = 0
keep_asking = True
while keep_asking:
    user_input = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if user_input == "espresso" or user_input == "latte" or user_input == "cappuccino":
        os.system("cls")
        if check_resources(MENU[user_input]["ingredients"]):
            print("Please insert coins.")
            quarter = float(input("how many quarters?: "))
            dime = float(input("how many dimes?: "))
            nickle = float(input("how many nickles?: "))
            pennie = float(input("how many pennies?: "))
            coffee_money = MENU[user_input]['cost']
            total_amount = 0.25 * quarter + 0.10 * dime + 0.05 * nickle + 0.01 * pennie 
            return_total= round(total_amount - coffee_money,2)
            if total_amount > coffee_money:
                money+=coffee_money
                update_resources(MENU[user_input]["ingredients"])
                print(f"Here is ${return_total} in change.")
                print(f"Here is your {user_input} ☕️. Enjoy!")
            elif total_amount == coffee_money:
                money+=coffee_money
                update_resources(MENU[user_input]["ingredients"])
                print(f"Here is your {user_input} ☕️. Enjoy!")
            else:    
                print(f"Sorry that's not enough money. Money refunded.")
    elif user_input == "report":
        report = f"Water: {resources['water']}ml\nMilk: {resources['milk']}ml\nCoffee: {resources['coffee']}g\nMoney: ${money}"
        print(report)
    elif user_input == "off":
        print("Turning off")
        keep_asking = False       
    else:
        print("Please type in a correct input and try again")      




