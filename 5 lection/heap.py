import heapq
import random
import string

xs = [(random.randrange(10), c) for c in string.ascii_uppercase[:5]]

heapq.heapify(xs)

print(f"Heapify: {xs}")

heapq.heappop(xs)

print(f"Popped {xs}")

heapq.heappush(xs, (2, 'X'))

print(f"Pushed: {xs}")
