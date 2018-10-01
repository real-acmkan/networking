import socket

# define some variables
target_host = "0.0.0.0"
target_port = 9999

#create a TCP socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((target_host, target_port)) # Connect to the specified host/port
client.send("GET / HTTP/1.1\r\nHost: 0.0.0.0\r\n\r\n") # Send message
response = client.recv(4096) # get the response from the server
print response # print the response from the server
