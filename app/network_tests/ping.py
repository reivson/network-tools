import subprocess

def perform_ping(target):
    """
    Perform a ping operation to the specified target.

    This function uses the system's ping command to send 4 ICMP echo requests to the target.

    Args:
        target (str): The IP address or hostname to ping.

    Returns:
        str: The output of the ping command or an error message if the command fails.
    """
    try:
        output = subprocess.check_output(['ping', '-c', '4', target], stderr=subprocess.STDOUT, universal_newlines=True)
        return output
    except subprocess.CalledProcessError as e:
        return f"Ping failed: {e.output}"