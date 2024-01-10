import socket

def connect_to_server(server_address, port):
    try:
        # Attempt to create a socket and connect to the server
        with socket.create_connection((server_address, port), timeout=5) as sock:
            print(f"Connected to {server_address} on port {port}")
            # Perform other operations here if needed
    except socket.error as e:
        print(f"Socket error: {e}")
    except ConnectionError as e:
        print(f"Connection error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Example usage:
server_address = "example.com"
port = 80

connect_to_server(server_address, port)
