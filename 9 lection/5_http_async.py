import sys
import random
import socket
import time
import selectors


def doubler_server(port=8080):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(("", port))
        s.setblocking(False)
        s.listen(5)

        sel = selectors.DefaultSelector()
        sel.register(s, selectors.EVENT_READ)
        while True:
            for key, mask in sel.select():
                if key.fileobj is s:
                    conn, addr = s.accept()
                    print("Connected by", addr)
                    conn.setblocking(False)
                    sel.register(conn, selectors.EVENT_READ, ("read", None))
                else:
                    conn = key.fileobj
                    op, arg = key.data
                    sel.unregister(conn)

                    if op == "read":
                        data = conn.recv(1024)
                        if not data:
                            conn.close()
                        n = int(data.decode())
                        res = f"{n * 2}\n".encode()
                        sel.register(conn, selectors.EVENT_WRITE, ("write", res))
                    elif op == "write":
                        conn.send(arg)
                        sel.register(conn, selectors.EVENT_READ, ("read", None))
                    else:
                        assert False, op


def doubler_client(port=8080):
    with socket.create_connection(("127.0.0.1", port)) as s:
        f = s.makefile(mode="rw", buffering=1, newline="\n")
        while True:
            n = random.randrange(10)
            f.write(f"{n}\n")
            print(n, f.readline().strip())
            time.sleep(random.random() * 2)


if __name__ == '__main__':
    if sys.argv[1] == "server":
        doubler_server()
    else:
        assert sys.argv[1] == "client"
        doubler_client(8080)
