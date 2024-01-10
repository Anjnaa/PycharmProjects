# def report():
#     print("pls insert coins")


class MoneyMachine:
    CURRENCY = "$"
    COIN_VALUE = {
        "quarters": 0.25,
        "dimes": 0.10,
        "nickles": 0.05,
        "pennies": 0.01
    }

    def __init__(self):
        self.profit = 0
        self.money_received = 0

    def report(self):
        """prints the current profit"""
        print(f"Money: {self.CURRENCY}{self.profit} ")

    def process_coins(self):
        """returns the total calculated fromm coins inserted. """
        print("please insert coins")
        for coin in self.COIN_VALUE:
            self.money_received += int(input(f"How many {coin}?: ")) * self.COIN_VALUE[coin]
        return self.money_received

    def make_payment(self, cost):
        self.process_coins()
        if self.money_received >= float(cost):
            change = round(self.money_received - float(cost), 2)
            print(f"Here is {self.CURRENCY}{change} in change. ")
            self.profit += float(cost)
            self.money_received = 0
            return True
        else:
            print("sorry that's not enough money. money refunded. ")
            self.money_received = 0
            return False