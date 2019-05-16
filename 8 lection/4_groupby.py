from itertools import groupby


def sorted_runs(xs):
    indices = range(len(xs) - 1)

    def is_increasing(idx):
        return xs[idx] < xs[idx + 1]

    return groupby(indices, is_increasing)


xs = [1, 2, 3, 5, 2, 0, 3, 1]

for is_increasing, group in sorted_runs(xs):
    print(
        "increase" if is_increasing else "decrease",
        sum(1 for _ in group),
    )
