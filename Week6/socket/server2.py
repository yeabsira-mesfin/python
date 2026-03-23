import socket

HOST = "0.0.0.0"
PORT = 1234

def recv_line(sock) -> bytes:
    """Read from sock until a newline b'\\n' is found. Returns the line WITHOUT the newline."""
    buffer = b""
    while True:
        chunk = sock.recv(1024)
        if not chunk:  # client disconnected
            return b""  # signal: no more data
        buffer += chunk

        if b"\n" in buffer:
            line, _rest = buffer.split(b"\n", 1)
            return line  # return one line (without \n)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(1)
    print(f"Server listening on {HOST}:{PORT}")

    conn, addr = s.accept()
    print("Connected by", addr)

    with conn:
        while True:
            line = recv_line(conn)
            if not line:
                break
            conn.sendall(b"ECHO: " + line + b"\n")

    print("Client disconnected. Server exiting.")
