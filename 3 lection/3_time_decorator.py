import time
import functools


def profile(f):
    @functools.wraps(f)
    def inner(*args, **kwargs):
        start = time.perf_counter()
        res = f(*args, **kwargs)
        elapsed = time.perf_counter() - start

        inner.__n_calls__ += 1
        inner.__total_time__ += elapsed

        return res

    inner.__n_calls__ = 0
    inner.__total_time__ = 0

    return inner


def memoize(f):
    cache = {}

    @functools.wraps(f)
    def inner(*args, **kwargs):
        key = (args, frozenset(kwargs.items()))
        if key not in cache:
            cache[key] = f(*args, **kwargs)

        return cache[key]

    return inner


@memoize
@profile
def fib(n):
    return 1 if n <= 1 else fib(n - 1) + fib(n - 2)


if __name__ == '__main__':
    print(fib(22))
    print(fib.__wrapped__.__total_time__)
    print(fib.__wrapped__.__n_calls__)
