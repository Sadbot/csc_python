import functools
import sys


def once(f):
    called = False

    def inner(*args, **kwargs):
        nonlocal called
        if not called:
            called = True
            res = f(*args, **kwargs)
            assert res is None
            return res

    return inner


@once
def init_logger():
    print('init logger')


def foo():
    init_logger()


if __name__ == '__main__':
    foo()
    foo()
