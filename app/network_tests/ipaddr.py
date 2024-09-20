import subprocess

def get_ip_addr():
    try:
        output = subprocess.check_output(['ip', 'addr'], stderr=subprocess.STDOUT, universal_newlines=True)
        return output
    except subprocess.CalledProcessError as e:
        return f"Failed to get IP address information: {e.output}"