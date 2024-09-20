import subprocess

def perform_traceroute(target):
    """
    Perform a traceroute operation to the specified target.

    This function uses the system's traceroute command to trace the route packets
    take to the target.

    Args:
        target (str): The IP address or hostname to traceroute.

    Returns:
        str: The output of the traceroute command or an error message if the command fails.
    """
    try:
        output = subprocess.check_output(['traceroute', target], stderr=subprocess.STDOUT, universal_newlines=True)
        return output
    except subprocess.CalledProcessError as e:
        return f"Traceroute failed: {e.output}"