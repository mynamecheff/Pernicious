import socket

def send_data(data, ip_address, port):
    try:
        # Create a socket object
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Connect to the server
        client_socket.connect((ip_address, port))

        # Encode the data to bytes (assuming ASCII encoding)
        data_bytes = data.encode('ascii')

        # Send the data
        client_socket.sendall(data_bytes)

        # Close the socket
        client_socket.close()
        print("Data sent successfully")
    except Exception as e:
        print(f"Error sending data: {e}")

if __name__ == "__main__":
    data_to_send = "Hello, World!"
    server_ip = "server_ip_address"
    server_port = 12345  # Replace with the actual port number

    send_data(data_to_send, server_ip, server_port)
