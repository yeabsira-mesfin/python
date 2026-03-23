import socket

HOST = "127.0.0.1"   # change to server IP if on another machine
PORT = 1234

def recv_line(sock) -> bytes:
    buffer = b""
    while True:
        chunk = sock.recv(1024)
        if not chunk:
            return b""
        buffer += chunk
        if b"\n" in buffer:
            line, _rest = buffer.split(b"\n", 1)
            return line

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    print("Connected. Type messages. Type [bye] to exit.")

    while True:
        msg = input("Me > ")
        s.sendall((msg + "\n").encode())

        reply = recv_line(s)
        if not reply:
            break
        print(reply.decode())

        if msg == "[bye]":
            break
