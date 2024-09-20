import os

def get_specific_env_var(var_name):
    """
    Retrieve the value of a specific environment variable.

    Args:
        var_name (str): The name of the environment variable to retrieve.

    Returns:
        str: The value of the environment variable or a message if not found.
    """
    return os.environ.get(var_name, f"Environment variable '{var_name}' not found")

def get_all_env_vars():
    """
    Retrieve all environment variables.

    Returns:
        dict: A dictionary containing all environment variables.
    """
    return dict(os.environ)