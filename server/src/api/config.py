import yaml
import os

from utils import get_project_root

class ComponentBaseConfigException(Exception):
    def __init__(self, message: str = None):
        super().__init__(message)


class ComponentConfig:

    api_base_path: str
    api_port: int

    def __init__(self, filename: str = None):
        self.read_config(filename)

    @staticmethod
    def build(filename: str = f"{get_project_root()}/resources/env.yaml"):
        return ComponentConfig(filename)

    def read_config(self, filename: str):

        try:
            with open(filename, 'r') as stream:
                config = yaml.safe_load(stream)
                self.api_base_path = config['server'].get("api-base-path")
                self.api_port = int(str(config['server'].get("api-port")))
        except Exception as exc:
            raise ComponentBaseConfigException(exc)
        