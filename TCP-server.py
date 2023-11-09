import socket
# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Bind the socket to the port localhost 1313:
server_address = ('localhost', 1313)
sock.bind(server_address)
#Listen for incoming client connections
while True:
    sock.listen(10)
    print('Waiting for a client to connect')
    client, address_port = sock.accept()
    print('Connection from client %s:%s' % address_port)
    # Receive request from the client
    request = client.recv(14)
    print('Client sent "%s"' % request.decode())
    reply = b'And Beyond!'
    print('Server replies "%s"' % reply.decode())
    client.sendall(reply)
# Close the client connection
client.close()