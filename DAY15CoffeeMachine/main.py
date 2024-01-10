MENU = {
    "espresso": {"ingredients": {"water": 50, "coffee": 18}, "cost": 1.5},
    "latte": {"ingredients": {"water": 50, "milk": 150, "coffee": 24}, "cost": 2.5},
    "cappuccino": {"ingredients": {"water": 50, "milk": 250, "coffee": 24}, "cost": 3.0}
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

profit = 0


def is_resources_sufficient(order_ingredients):
    for item in order_ingredients:
        # print(order_ingredients[item])
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough{item}")
            return False
        return True


def process_coins():
    print("Please insert coins.")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total

def is_transaction_successful(money_received, drink_cost):
    if money_received >= drink_cost:
        change = round(money_received-drink_cost, 2)
        print(f"Here is ${change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("sorry that's not enough money. Money refunded")
        return False

def make_coffee(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name}, Enjoy Coffee!")


is_on = True
while is_on:
    choice = input("what would you like? (espresso/latte/cappuccino): ")

    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water:{resources['water']}ml")
        print(f"Milk:{resources['milk']}ml")
        print(f"Coffee:{resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        drink = MENU[choice]
        # print(drink)
        # print(drink["cost"])
        if is_resources_sufficient(drink["ingredients"]):
            payment = process_coins()
        if is_transaction_successful(payment, drink["cost"]):
            make_coffee(choice, drink["ingredients"])
