import os
from api_utils import get_project_root

class ComponentBaseConfigException(Exception):
    def __init__(self, message: str = None):
        super().__init__(message)


class ComponentConfig:

    api_port: int

    scheme: str
    address: str
    port: str
    user: str
    password: str

    def __init__(self):
        self.read_config()

    @staticmethod
    def build():
        return ComponentConfig()

    def read_config(self):

        try:
            self.api_port = os.getenv("API_PORT")
            self.scheme = os.getenv("DATABASE_SCHEME")
            self.address = os.getenv("DATABASE_ADDRESS")
            self.port = os.getenv("DATABASE_PORT")
            self.user = os.getenv("DATABASE_USER")
            self.password = os.getenv("DATABASE_PASSWROD")
            # os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = get_project_root() + '/' + os.getenv("GOOGLE_APPLICATION_CREDENTIALS")
                
        except Exception as exc:
            raise ComponentBaseConfigException(exc)
        