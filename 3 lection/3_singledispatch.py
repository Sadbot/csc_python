import functools


@functools.singledispatch
def json(x):
    assert False, f"json not supported for {type(x)}"


@json.register(type(None))
def _(x):
    return "null"


@json.register(int)
def _(x):
    return str(x)


@json.register(list)
def _(xs):
    content = ', '.join(json(x) for x in xs)
    return f"[{content}]"

print(json(None))
print(json(92))
print(json([92, None]))
