import socket

def scan_port(host, port):
    """
    Attempt to connect to a specific port on the given host.

    Args:
        host (str): The hostname or IP address to scan.
        port (int): The port number to attempt to connect to.

    Returns:
        str: A message indicating whether the port is open or closed.
    """
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((host, port))
        if result == 0:
            return f"Port {port} is open"
        else:
            return f"Port {port} is closed"
    except socket.error:
        return f"Couldn't connect to {host}"
    finally:
        sock.close()

def scan_ports(host, start_port, end_port):
    """
    Scan a range of ports on the given host.

    Args:
        host (str): The hostname or IP address to scan.
        start_port (int): The first port in the range to scan.
        end_port (int): The last port in the range to scan.

    Returns:
        list: A list of strings, each indicating the status of a port.
    """
    results = []
    for port in range(start_port, end_port + 1):
        results.append(scan_port(host, port))
    return results