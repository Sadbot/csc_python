import functools
import sys

DEBUG = True


def trace(f=None, *, stream=sys.stdout):
    if f is None:
        return functools.partial(trace, stream=stream)

    if not DEBUG:
        return f

    @functools.wraps(f)
    def inner(*args, **kwargs):
        call = ', '.join(
            [str(a) for a in args] + [f"{k} =  {v}" for k, v in kwargs]
        )
        print(f"{f.__name__}({call}) = ...", file=stream)
        res = f(*args, **kwargs)
        print(f"{f.__name__}({call}) = {res}", file=stream)
        return res

    return inner


@trace(stream=sys.stderr)
def max(*args):
    """Finds the largest argument"""
    ret = 0
    for x in args:
        ret = ret if x < ret else x
    return ret


help(max)
max(-10, -1, -3)

