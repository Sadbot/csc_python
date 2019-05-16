from asyncio import coroutine


@coroutine
def printer():
    try:
        while True:
            item = yield
            print(item)
    finally:
        print("Cleaning up")


p = printer()
p.send(None)
p.send(92)
p.close()
