import socket

host_name = socket.gethostname()
ip_address = socket.gethostbyname(host_name)

print(f"""
This is the host name: {host_name}
This is the ip address: {ip_address} 
      """)