import subprocess

def get_ip_addr():
    """
    Retrieve IP address information using the 'ip addr' command.

    This function uses subprocess to run the 'ip addr' command and capture its output.

    Returns:
        str: The output of the 'ip addr' command or an error message if the command fails.
    """
    try:
        output = subprocess.check_output(['ip', 'addr'], stderr=subprocess.STDOUT, universal_newlines=True)
        return output
    except subprocess.CalledProcessError as e:
        return f"Failed to get IP address information: {e.output}"