def chain(*xss):
    for xs in xss:
        yield from xs


xs = [1, 2, 3]
ys = [92]

print(*chain(xs, ys))
