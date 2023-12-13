import os

def fetch_current_directory():
    return os.path.dirname(os.path.realpath(__file__))
