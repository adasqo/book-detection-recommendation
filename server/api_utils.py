# from pathlib import Path
import os

def get_project_root():
    # return Path(__file__).parent
    return os.path.dirname(os.path.abspath(__file__))