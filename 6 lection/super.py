import functools


class ProxyClass:
    def __init__(self, cls, obj):
        self.__cls = cls
        self.__obj = obj

    def __getattr__(self, item):
        item = getattr(self.__cls, item)

        if callable(item):
            item = functools.partial(item, self.__obj)
        return item


def _super(cls, obj):
    mro = type(obj).mro()
    super_cls = mro[mro.index(cls) + 1]

    return ProxyClass(super_cls, obj)


class Base:
    def f(self):
        print("Base")


class A(Base):
    def f(self):
        print("A", end=', ')
        _super(A, self).f()


class B(Base):
    def f(self):
        print("B", end=', ')
        _super(B, self).f()


class C(A, B):
    pass


C().f()
