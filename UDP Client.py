import socket

# declare global variables
target_host = "127.0.0.1"
target_port = 80

# create UDP socket
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# send message to the defined host/port
client.sendto("AAABBBCCC", (target_host, target_port))

data, addr = client.recvfrom(4t096)

print data
