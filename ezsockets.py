def server(port, action):
    import socket

    # Create a TCP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Bind the socket to the port
    server_address = ('localhost', port)
    sock.bind(server_address)
    # Listen for incoming connections
    sock.listen(1)

    while True:
        # Wait for a connection
        connection, client_address = sock.accept()
        try:

            # Receive the data in small chunks and retransmit it
            while True:
                data = connection.recv(16)
                a = data
                data = a.decode()
                exec(action)

        except:
            print("Client disconected")
def client(host, port, data):
    import socket
    import sys

    # Create a TCP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect the socket to the port where the server is listening
    server_address = (host, port)
    sock.connect(server_address)
    try:
        # Send data
        message = data
        message = "" + message
        message = message.encode()
        sock.sendall(message)

        # Look for the response
        amount_received = 0
        amount_expected = len(message)

        while amount_received < amount_expected:
            data = sock.recv(16)
            amount_received += len(data)

    finally:
        sock.close()
