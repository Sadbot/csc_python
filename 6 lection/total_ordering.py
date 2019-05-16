import functools


@functools.total_ordering
class Counter:
    def __init__(self, initial_count=0):
        self.count = initial_count

    def increment(self):
        self.count += 1

    def __lt__(self, other):
        assert isinstance(other, Counter)

        return self.count < other.count

    def __gt__(self, other):
        assert isinstance(other, Counter)

        return self.count > other.count


c1 = Counter(92)
c2 = Counter(62)

print(f"c1 > c2 = {c1 > c2}")
print(f"c1 >= c2 = {c1 >= c2}")
print(f"c1 < c2 = {c1 < c2}")
print(f"c1 <= c2 = {c1 <= c2}")
print(f"c1 == c2 = {c1 == c2}")
print(f"c1 != c2 = {c1 != c2}")
