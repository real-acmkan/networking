# more changes will be made
# this just creates a basic TCP server that waits for a client to connect
# ideally this is supposed to be used for testing TCP connections on a small network


import socket
import threading

# define global variables
bind_ip = "0.0.0.0"
bind_port = 9999

# create socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind((bind_ip, bind_port))

server.listen(5)

# show interface that is being listened on
print "[*] Listening on %s:%d" % (bind_ip, bind_port)


def handle_client(client_socket):
		
	request = client_socket.recv(1024)
	
  # show message from client
	print "[*] Received: %s" % request
	
  # send message to client
	client_socket.send(raw_input())
	
  # close socket
	client_socket.close()
	
while True:
	
  # accept all incoming connections
	client, addr = server.accept()
	
  # show incoming connection and message
	print "[*] Accepted connection from: %s:%d" % (addr[0], addr[1])
	
  # use threading to call on def handle_client with arguments
	client_handler = threading.Thread(target=handle_client, args=(client,))
	client_handler.start()
