# Import socket module
import socket            

# Create a socket object
s = socket.socket()        
 
# Define the port on which you want to connect
host = '192.168.1.9'
port = 80               

for i in range(0,10):     
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host,port))
        s.sendall(b"Hello, world")
        data = s.recv(1024)
        print(f"Received {data!r}")
        s.close()


