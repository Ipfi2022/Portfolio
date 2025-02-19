class Cash:
    def __init__(self, twenties, fifties):
        self._twenties = twenties
        self._fifties = fifties

    @property
    def twenties(self):
        return self._twenties

    @twenties.setter
    def twenties(self, value):
        if (str(value)).isdigit():
            self._twenties = int(value)
        else:
            raise ValueError("Value must be a positive or null integer")

    @property
    def fifties(self):
        return self._fifties

    @fifties.setter
    def fifties(self, value):
        if (str(value)).isdigit():
            self._fifties = int(value)
        else:
            raise ValueError("Value must be a positive or null integer")

    def total_cash(self):
        return ((self.twenties)*20)+((self.fifties)*50)

wallet1 = Cash(3,4)
print(wallet1.twenties)
print(wallet1.fifties)
print(wallet1.total_cash())


wallet1.twenties = 7
print(wallet1.twenties)
wallet1.fifties = 8
print(wallet1.fifties)
print(wallet1.total_cash())


wallet1.twenties = 2
print(wallet1.twenties)
#wallet1.fifties = -5
print(wallet1.fifties)
print(wallet1.total_cash())

wallet2 = Cash(3,-4) # Note that a negative amount of fifties is allowed!
print(wallet2.twenties)
print(wallet2.fifties)
print(wallet2.total_cash())
