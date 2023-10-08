import socket
import ssl
import sys
import threading

# Code reference: https://docs.python.org/3.3/library/ssl.html

# Provide a socket for server to connect to client
def ready_for_server():
    server_port, server_crt, server_key = int(sys.argv[1]), sys.argv[2], sys.argv[3]
    # create the server address
    server_address = ('', server_port)
    # Create a socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Bind the socket to the port
    sock.bind(server_address)
    # Listen for incoming connections
    sock.listen(100)
    # Create a SSL context with TLS protocol
    context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
    # Load the server certificate and private key
    context.load_cert_chain(certfile=server_crt, keyfile=server_key)
    return sock, context

# Handle the data from client
def handle_client(ssl_sock):
    try:
        while True:
            # Receive data from client
            data = ssl_sock.recv(1024)
            if data:
                print("Received: ", data)
                # when receive data, send back a message
                message = input("Enter message: ")
                message = ("Server: " + message + "\n").encode()
                ssl_sock.sendall(message)
            else:
                break
    except Exception as e:
        print("Error while receiving: ", e)
    except KeyboardInterrupt:
        print("Have a good time! ")
    finally:
        ssl_sock.close()

# Server main function
def server():
    # Prepare the socket and context
    sock, context = ready_for_server()
    try:
        while True:
            
            # connect with client, check the certificate
            print("Waiting for client...")
            connection, client_address = sock.accept()
            print("Client connected: ", client_address)
            
            # wrap the socket with SSL context
            ssl_socket = context.wrap_socket(connection, server_side=True)
            
            # create a thread to handle the client
            client_thread = threading.Thread(target=handle_client, args=(ssl_socket,))
            client_thread.start()
            
    except Exception as e:
        print("Error while accepting: ", e)
    except KeyboardInterrupt:
        print("Have a good time! ")
    finally:
        sock.close()
        sys.exit(1)
        
server()
