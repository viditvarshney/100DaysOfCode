import time


class MoneyMachine:

    CURRENCY = "₹"

    COIN_VALUES = {
        "Rupees": 1,
        "Paisa": 0.01
    }

    def __init__(self):
        self.profit = 0
        self.money_received = 0

    def report(self):
        """Prints the current profit"""
        print(f"Money: {self.CURRENCY}{self.profit}")

    def process_coins(self):
        """Returns the total calculated from coins inserted."""
        print("Please insert coins.")
        for coin in self.COIN_VALUES:
            self.money_received += int(
                input(f"How many {coin}?: ")) * self.COIN_VALUES[coin]
        print("Transacting...")
        time.sleep(3)
        return self.money_received

    def make_payment(self, cost):
        """Returns True when payment is accepted, or False if insufficient."""

        print(f"Money Received: {self.process_coins()}")
        time.sleep(2)

        if self.money_received >= cost:
            change = round(self.money_received - cost, 2)
            print(f"Here is {self.CURRENCY}{change} in change.")
            self.profit += cost
            self.money_received = 0
            return True
        else:
            print("Sorry that's not enough money. Money refunded.")
            self.money_received = 0
            return False
