import sys
import random
import socket
import time
from threading import Thread


def doubler_server(port=8080):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(("", port))
        s.setblocking(False)
        s.listen(5)
        while True:
            try:
                conn, addr = s.accept()
            except BlockingIOError:
                continue
            t = Thread(target=handle_connection, args=(conn, addr))
            t.start()


def handle_connection(conn, addr):
    print("Connected by", addr)
    with conn:
        while True:
            data = conn.recv(1024)
            if not data:
                break
            n = int(data.decode())
            res = f"{n * 2}\n".encode()
            conn.send(res)

    print("disconnected by:", addr)


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
