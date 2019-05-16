import functools


def min(xs):
    return functools.reduce(lambda x, y: x if x <= y else y, xs, float('inf'))


print(min([0, 1, 2]))
