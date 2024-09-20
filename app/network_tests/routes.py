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
    output = perform_ping(target)
    return Response(output, mimetype='text/plain')

@bp.route('/traceroute/<target>')
def traceroute(target):
    output = perform_traceroute(target)
    return Response(output, mimetype='text/plain')

@bp.route('/telnet/<host>/<int:port>')
def telnet(host, port):
    output = perform_telnet(host, port)
    return Response(output, mimetype='text/plain')

@bp.route('/ipaddr')
def ipaddr():
    output = get_ip_addr()
    return Response(output, mimetype='text/plain')

@bp.route('/env/<var_name>')
def check_specific_env(var_name):
    value = get_specific_env_var(var_name)
    return jsonify({var_name: value})

@bp.route('/env')
def check_all_env():
    all_vars = get_all_env_vars()
    return jsonify(all_vars)


@bp.route('/dns/<domain>')
def dns_resolve(domain):
    result = dns_lookup(domain)
    return jsonify({"result": result})

@bp.route('/portscan/<host>')
def port_scan(host):
    start_port = request.args.get('start', default=1, type=int)
    end_port = request.args.get('end', default=1024, type=int)
    results = scan_ports(host, start_port, end_port)
    return jsonify({"results": results})