import socket

hs= socket.gethostname()
HOST = socket.gethostbyname(hs)
PORT = 1234

with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    for i in range(5):
        data = input("Please enter any string")
        s.send(data.encode())
        reply = s.recv(1024)        
        print(reply.decode())
        