from json import encoder
import os
from time import sleep
import connexion as connexion
from src.database.client import ElasticsearchClient
from src.cleaner.task_cleaner import TaskCleaner
from src.main.models_utils.detection_model import BooksDetectionModel
from src.api.config import ComponentConfig
from api_utils import get_project_root
from flask_cors import CORS

def start_api():
    config = ComponentConfig.build()
    base_path = os.path.join(get_project_root(), "resources/openapi/")
    app = connexion.App(__name__, specification_dir=base_path, options={"swagger_ui": True})
    CORS(app.app)
    app.app.json_encoder = encoder.JSONEncoder  
    app.add_api("swagger.yaml")
    
    sleep(20)
    BooksDetectionModel.initiate_detection_model()
    TaskCleaner(ElasticsearchClient()).start()

    app.run(port=config.api_port)
    return app.app
