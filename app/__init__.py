from flask import Flask
from .config import Config

def create_app(config_class=Config):

    """
    Creates the Flask application instance.

    :param config_class: The configuration class to use.
    :type config_class: Config

    :return: The Flask application instance.
    :rtype: Flask
    """

    app = Flask(__name__)
    app.config.from_object(config_class)

    from .network_tests import bp as network_tests_bp
    app.register_blueprint(network_tests_bp)

    @app.route('/')
    def home():
        message = """
        <h3>How to use this application</h3>

        <p>Use <code>/network/ping/[target]</code> to ping a target.</p>
        <p>Use <code>/network/traceroute/[target]</code> to trace a target.</p>
        <p>Use <code>/network/telnet/[host]/[port]</code> to connect to a host and port.</p>
        <p>Use <code>/network/ipaddr</code> to get the IP address of the container.</p>
        <p>Use <code>/network/env/[var_name]</code>, or <code>/network/env</code> to check environment variables.</p>
        <p>Use <code>/network/dns/[domain]</code> to check the DNS entry for [domain].</p>
        <p>Use <code>/network/portscan/[host]?start=[start_port]&end=[end_port]</code> to scan ports on [host].</p>
        """
        return message

    return app