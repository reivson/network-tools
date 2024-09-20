import socket

def dns_lookup(domain):
    try:
        ip_address = socket.gethostbyname(domain)
        return f"The IP address of {domain} is {ip_address}"
    except socket.gaierror:
        return f"Unable to resolve {domain}"