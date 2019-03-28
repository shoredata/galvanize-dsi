"""Coffee Cup"""


class CoffeeCup(object):
    """Cup of coffee."""

    def __init__(self, capacity=12, coffee_amt=12,
                 sip_size=0.5, gulp_size=1):
        """Create a new CoffeeCup.

        Arguments
        ---------
        capacity : float
            The size of the coffee cup in fluid ounces.
        coffee_amt : float
            The initial quantity of coffee in the cup in fl. oz.
        sip_size: float
            Amount of coffee consumed in one sip.
        gulp_size: float
            Amount of coffee consumed in one gulp.
        """
        self.capacity = capacity
        self.coffee_amt = coffee_amt
        self.sip_size = sip_size
        self.gulp_size = gulp_size

    def __str__(self):
        """Return a text description of the CoffeeCup."""
        return "{}oz Coffee cup containing {}oz of coffee.".format(
            self.capacity, self.coffee_amt)

    def sip(self):
        """Take one sip of the coffee."""
        self.drink(self.sip_size)

    def gulp(self):
        """Take one gulp of the coffee."""
        self.drink(self.gulp_size)

    def drink(self, amount_to_drink):
        """Drink the specified amount of coffee.
        If less than the specified amount remains, drink the rest."""
        if self.coffee_amt == 0:
            raise Exception("Out of Coffee!!!")
        elif self.coffee_amt < amount_to_drink:
            self.coffee_amt = 0
        else:
            self.coffee_amt -= amount_to_drink

    def fill(self):
        """Pour coffee into the cup."""
        if self.coffee_amt == self.capacity:
            raise Exception("Thy cup runneth over!")
        else:
            self.coffee_amt = self.capacity

    def pour_out(self):
        """Empty the cup of coffee completely."""
        self.coffee_amt = 0


def play_game():
    """Play a game involving coffee drinking."""

    cup = CoffeeCup()

    while cup.coffee_amt > 0:
        print("You have a {}".format(str(cup)))
        action = raw_input("Do you want to sip, gulp, fill, or pour out? ")
        if action == "sip":
            cup.sip()
        elif action == "gulp":
            cup.gulp()
        elif action == "fill":
            cup.fill()
        elif action == "pour out" or action == "pour_out":
            cup.pour_out()

    print("You are out of coffee. Game over!")
