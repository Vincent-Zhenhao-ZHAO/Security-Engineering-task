import socket
import ssl
import sys

registed_url, ca_crt, client_port  = sys.argv[1], sys.argv[2], int(sys.argv[3])

# Code reference: https://docs.python.org/3.3/library/ssl.html

# Provide a socket for client to connect to server
def ready_for_client():
    
    # Create a socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Create a SSL context with TLS protocol
    context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
    
    # Load the client certificate
    context.load_verify_locations(ca_crt)
    
    # Require certificate from server
    context.verify_mode = ssl.CERT_REQUIRED

    # Wrap socket with SSL context
    connect_ssl = context.wrap_socket(sock, server_hostname=registed_url)

    return connect_ssl

# Handle the data from server
def handle_with_data(message, connect_ssl):
    try:
        connect_ssl.sendall(message)
        data = connect_ssl.recv(1024)
        print("Received: ", data)
    except Exception as e:
        print("Error while receiving: ", e)
    except KeyboardInterrupt:
        print("Have a good time! ")

# Client main function
def client():
    # if first time, send a hello message
    # if not, send the message from input
    count = 0
    connect_ssl = ready_for_client()
    
    # Connect to server
    try:
        connect_ssl.connect((registed_url, client_port))
    except Exception as e:
        print("Error while connecting: ",e)
        connect_ssl.close()
        sys.exit(1)
    except KeyboardInterrupt:
        print("Have a good time! ")
        connect_ssl.close()
        sys.exit(1)

    # Send message to server
    try:    
        while True:
            count += 1
            if count > 1:
                message = input("Enter message: ")
                message = ("Client: " + message + "\n").encode()
            elif count == 1:
                message = b"Client: Hello, I am client from machine A."
            elif message == "vincentexit":
                message = b"Client: Vncent has left the chat."
                handle_with_data(message, connect_ssl)
                break
            handle_with_data(message, connect_ssl)
    finally:
        connect_ssl.shutdown(socket.SHUT_RDWR)
        connect_ssl.close()

client()
