import socket
import time

def perform_telnet(host, port):
    try:
        start_time = time.time()
        with socket.create_connection((host, port), timeout=10) as sock:
            end_time = time.time()
        return f"Successfully connected to {host} on port {port}. Time taken: {end_time - start_time:.2f} seconds"
    except socket.error as e:
        return f"Telnet failed: {str(e)}"