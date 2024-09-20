import os

def get_specific_env_var(var_name):
    return os.environ.get(var_name, f"Environment variable '{var_name}' not found")

def get_all_env_vars():
    return dict(os.environ)