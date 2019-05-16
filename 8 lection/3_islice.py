from itertools import islice

xs = range(10)

assert list(islice(xs, 2, 8, 3)) == [2, 5]

# Part 2

from itertools import count, cycle, repeat, islice


def take(n, xs):
    return list(islice(xs, 0, n))


assert take(3, count(start=1, step=2)) == [1, 3, 5]
assert take(3, cycle(["любит", "не любит"])) == ["любит", "не любит", "любит"]

assert take(3, repeat(92)) == list(repeat(92, times=3))

# Part 3

from itertools import dropwhile, takewhile

assert list(dropwhile(lambda x: x < 5, range(10))) == [5, 6, 7, 8, 9]

# Part 4

from itertools import chain

xs = (range(0, i) for i in range(1000))

print(sum(chain.from_iterable(xs)))

# Part 5

from itertools import tee

it = range(3)

a, b, c = tee(it, 3)

assert list(a) == list(b) == list(c) == [0, 1, 2]

# Part 6

from itertools import product, combinations, permutations
from itertools import combinations_with_replacement

print('part 6')

print('product:', *product("AB", repeat=2))

print('combinations:', *combinations(range(5), 2))


# Формирование графа соответствующих по длине слов
def build_graph(words, mismatch_percent):
    for (i, u), (j, v) in combinations(enumerate(words), 2):
        if len(u) != len(v):
            continue

    print('kek lol')
