from json import encoder
import os
import connexion as connexion
from src.api.config import ComponentConfig
from utils import get_project_root
from flask_cors import CORS

def start_api():
    config = ComponentConfig.build()
    base_path = os.path.join(get_project_root(), "resources/openapi/")
    app = connexion.App(__name__, specification_dir=base_path, options={"swagger_ui": True})
    CORS(app.app)
    app.app.json_encoder = encoder.JSONEncoder  
    app.add_api("swagger.yaml", base_path=config.api_base_path)
    app.run(port=config.api_port)
    return app.app
