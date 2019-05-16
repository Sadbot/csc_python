import functools


def doubling(cls):
    orig_increment = cls.increment

    @functools.wraps(orig_increment)
    def increment(self):
        orig_increment(self)
        orig_increment(self)

    cls.increment = increment

    return cls


class Counter:
    def __init__(self, initial_count=0):
        self.count = initial_count

    def increment(self):
        self.count += 1


@doubling
class DoublingCounter(Counter):
    pass


c = DoublingCounter()
assert c.count == 0

c.increment()
assert c.count == 2
