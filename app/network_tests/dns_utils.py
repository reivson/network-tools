import socket

def dns_lookup(domain):
    """
    Perform a DNS lookup for the given domain.

    This function attempts to resolve the IP address of the specified domain
    using Python's socket library.

    Args:
        domain (str): The domain name to resolve.

    Returns:
        str: A string containing either the resolved IP address or an error message.
    """
    try:
        ip_address = socket.gethostbyname(domain)
        return f"The IP address of {domain} is {ip_address}"
    except socket.gaierror:
        return f"Unable to resolve {domain}"