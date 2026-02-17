import time, socket, sys

print("setup Server")
soc = socket.socket()
host_name = socket.gethostname()
ip = socket.gethostbyname(host_name)

port = 1234
soc.bind((host_name,port))

print(f"{host_name} {ip}")

name = input("Enter name: ")
soc.listen(1)

print("Waiting for incoming connections...")
connection, addr = soc.accept()

print(f"Received connection from, addr[0], {addr[1]} \n")
print(f"Connection Established. connected from: {format(addr[0],str(addr[1]))}")

client_name = connection.recv(1024)
client_name = client_name.decode()

print(client_name + 'Has Connected')
print(f"Press [bye] to leave the chat room")

while True:
    message = input("Me >")
    if message == '[bye]':
        message = "Good Night..."
        connection.send(message.encode())
        print("\n")
        break
    connection.send(message.encode())
    message = connection.recv(1024)
    message = message.decode()
    print(client_name,'>', message)