import socket
import time

def perform_telnet(host, port):
    """
    Attempt to establish a Telnet connection to the specified host and port.

    This function tries to create a TCP connection to simulate a Telnet connection.
    It measures the time taken to establish the connection.

    Args:
        host (str): The hostname or IP address to connect to.
        port (int): The port number to connect to.

    Returns:
        str: A message indicating the success or failure of the connection attempt,
             including the time taken if successful.
    """
    try:
        start_time = time.time()
        with socket.create_connection((host, port), timeout=10) as sock:
            end_time = time.time()
        return f"Successfully connected to {host} on port {port}. Time taken: {end_time - start_time:.2f} seconds"
    except socket.error as e:
        return f"Telnet failed: {str(e)}"