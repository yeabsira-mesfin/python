import socket 
def test():
    host_name = socket.gethostname()
    host_ip = socket.gethostbyname(host_name)
    print(f"""
Host Name: {host_name}
IP: {host_ip}
""")
    
if __name__ == "__main__":
    test()