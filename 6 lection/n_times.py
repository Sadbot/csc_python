import functools


class n_times:
    def __init__(self, n=1):
        self.n = n

    def __call__(self, f):
        @functools.wraps(f)
        def inner(*args, **kwargs):
            for _ in range(self.n):
                f(*args, **kwargs)

        return inner
