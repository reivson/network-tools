from flask import Response, jsonify
from . import bp
from .ping import perform_ping
from .traceroute import perform_traceroute
from .telnet import perform_telnet
from .ipaddr import get_ip_addr
from .envcheck import get_specific_env_var, get_all_env_vars
from .dns_utils import dns_lookup
from .port_scanner import scan_ports

@bp.route('/ping/<target>')
def ping(target):
    """
    Endpoint to perform a ping operation.

    Args:
        target (str): The IP address or hostname to ping.

    Returns:
        Response: A Flask Response object containing the ping results.
    """
    output = perform_ping(target)
    return Response(output, mimetype='text/plain')

@bp.route('/traceroute/<target>')
def traceroute(target):
    """
    Endpoint to perform a traceroute operation.

    Args:
        target (str): The IP address or hostname to traceroute.

    Returns:
        Response: A Flask Response object containing the traceroute results.
    """
    output = perform_traceroute(target)
    return Response(output, mimetype='text/plain')

@bp.route('/telnet/<host>/<int:port>')
def telnet(host, port):
    """
    Endpoint to perform a telnet operation.

    Args:
        host (str): The hostname or IP address to connect to.
        port (int): The port number to connect to.

    Returns:
        Response: A Flask Response object containing the telnet results.
    """
    output = perform_telnet(host, port)
    return Response(output, mimetype='text/plain')

@bp.route('/ipaddr')
def ipaddr():
    """
    Endpoint to retrieve IP address information.

    Returns:
        Response: A Flask Response object containing the IP address information.
    """
    output = get_ip_addr()
    return Response(output, mimetype='text/plain')

@bp.route('/env/<var_name>')
def check_specific_env(var_name):
    """
    Endpoint to retrieve a specific environment variable.

    Args:
        var_name (str): The name of the environment variable to retrieve.

    Returns:
        Response: A Flask Response object containing the environment variable value.
    """
    value = get_specific_env_var(var_name)
    return jsonify({var_name: value})

@bp.route('/env')
def check_all_env():
    """
    Endpoint to retrieve all environment variables.

    Returns:
        Response: A Flask Response object containing all environment variables.
    """
    all_vars = get_all_env_vars()
    return jsonify(all_vars)


@bp.route('/dns/<domain>')
def dns_resolve(domain):
    """
    Endpoint to perform a DNS lookup.

    Args:
        domain (str): The domain name to resolve.

    Returns:
        Response: A Flask Response object containing the DNS lookup results.
    """
    result = dns_lookup(domain)
    return jsonify({"result": result})

@bp.route('/portscan/<host>')
def port_scan(host):
    """
    Endpoint to perform a port scan.

    Args:
        host (str): The hostname or IP address to scan.

    Query Parameters:
        start (int): The starting port number (default: 1)
        end (int): The ending port number (default: 1024)

    Returns:
        Response: A Flask Response object containing the port scan results.
    """
    start_port = request.args.get('start', default=1, type=int)
    end_port = request.args.get('end', default=1024, type=int)
    results = scan_ports(host, start_port, end_port)
    return jsonify({"results": results})