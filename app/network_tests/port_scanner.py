import socket

def scan_port(host, port):
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
    results = []
    for port in range(start_port, end_port + 1):
        results.append(scan_port(host, port))
    return results