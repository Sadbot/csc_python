class Counter:
    def __init__(self, initial_count=0):
        self.count = initial_count

    def increment(self):
        self.count += 1

    def __repr__(self):
        return f"Counter({self.count}"

    def __str__(self):
        return f"{self.count}"

    def __format__(self, format_spec):
        if format_spec == "bold":
            return f"**{self.count}**"
        return str(self.count)


c = Counter(92)

print(f"{c:bold}")

assert f"{c:bold}" == "**92**"
