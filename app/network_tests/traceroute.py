import subprocess

def perform_traceroute(target):
    try:
        output = subprocess.check_output(['traceroute', target], stderr=subprocess.STDOUT, universal_newlines=True)
        return output
    except subprocess.CalledProcessError as e:
        return f"Traceroute failed: {e.output}"