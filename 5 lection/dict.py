graph = {}


def add_edge(u, v):
    graph.setdefault(u, []).append(v)


def neighbours(u):
    graph.get(u, [])


# Part 2

from collections import defaultdict

graph = defaultdict(set)

graph[2].add(2)
graph[2].add(1)
graph[3].add(3)

print(graph)

# Part 3

from collections import Counter


def count_words(text):
    return Counter(text.split())


words = count_words(open(__file__).read())

for word, count in words.most_common(3):
    print(f"{word:<5}: {count}")

# Part 4

c = Counter(a=3, b=1)
d = Counter(a=1, b=2)

print(f"plus: {c + d}")
print(f"diff: {c - d}")
print(f"intersect: {c & d}")
print(f"union: {c | d}")

# Part 5

print('part 5')

c = Counter()

c[92] = -10

print(f"{c}")

c[92] += 1

print(f'+1: {c}')
c.update([92])

print(f'Update: {c}')

print(f"unar operation: {+c}")

print(f'after unar: {c}')


# part 6

print('part 6')

from collections import ChainMap

locals = {}
globals = {'foo': 92}
builtins = {'bar': 93}


scope = ChainMap(locals, globals, builtins)

print(f"scope['foo'] = {scope['foo']}")

scope['foo'] = 1

print(f"globals = {globals}")

print(f"locals = {locals}")

print(f"scope.maps = {scope.maps}")
