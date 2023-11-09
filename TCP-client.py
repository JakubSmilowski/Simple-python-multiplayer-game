import socket
import time
# Create a TCP/IP socket
while True:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Connect to the server listening at localhost:1313
    server_address = ('localhost', 1313)
    print('Connecting to %s:%s' % server_address)
    sock.connect(server_address)
    # Send request message
    message = b'To Infinity...'
    print('Client sendng "%s"' % message.decode())
    sock.sendall(message)
    # Receive reply from server
    reply = sock.recv(11)
    print('Client received "%s"' % reply.decode())
    sock.close()
    time.sleep(5)
    # Close the server connection
