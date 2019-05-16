class Counter:
    def __init__(self, initial_count=0):
        self.count = initial_count

    def increment(self):
        self.count += 1

    @property
    def is_zero(self):
        return self.count == 0


c = Counter()

assert c.is_zero

c.increment()

assert not c.is_zero


class Temperature:
    def __init__(self, *, celsius=0):
        self.celsius = celsius

    @property
    def fahrenheit(self):
        return self.celsius * 9 / 5 + 32

    @fahrenheit.setter
    def fahrenheit(self, value):
        self.celsius = (value - 32) * 5 / 9

    @fahrenheit.deleter
    def fahrenheit(self):
        del self.celsius


c = Temperature()
c.fahrenheit = 451
assert c.celsius == 232.77777777777777
