import os
from dotenv import load_dotenv, dotenv_values

def load_all_env_as_dict() -> dict:
    load_dotenv()
    return {key: os.getenv(key) for key in os.environ.keys()}

def load_env_as_dict(env_file_path: str) -> dict:
    return dotenv_values(env_file_path)