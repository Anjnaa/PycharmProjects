class CoffeeMaker:
    resources = {
        "water": 500,
        "milk": 400,
        "coffee": 100
    }

    def report(self):
        print(f"Water:{self.resources['water']}ml")
        print(f"Milk:{self.resources['milk']}ml")
        print(f"Coffee:{self.resources['coffee']}g")

    def is_resources_sufficient(self, drink):
        can_make = True
        for item in drink.ingredients:
            if int(drink.ingredients[item]) > self.resources[item]:
                print(f"sorry, there is not enough{item}. ")
        return can_make

    def make_coffee(self, order):
        for item in order.ingredients:
            self.resources[item] -= int(order.ingredients[item])
        print(f"Here is your {order.name}.Enjoy! ")
