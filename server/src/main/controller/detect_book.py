import base64
import json
import logging
import os

import cv2
from src.main.utils.image_manager import ImageManager
from src.database.task_status import TaskStatus

from src.database.client import ElasticsearchClient

class DetectBookController:

    logger = logging.getLogger()

    def __init__(self) -> None:
        self.elastic_client = ElasticsearchClient()

    def detect_book(self, task_id: str, book_id: str): 
        
        try:
            image_path = f"./images/{task_id}.jpg"

            task = self.elastic_client.get_task(task_id)
            details = task["details"]
            image = details["image"]
            objects = details["books"]
            
            image = self.convert_image(image)
            self.dump_image(image, image_path)

            book_coordinates = self.find_book_coordinates(book_id, objects)
            image = self.draw_coordinates(image_path, book_coordinates)

            self.elastic_client.update_task_status(task_id, TaskStatus.PROCESSING.value)
            self.elastic_client.close()
            
            return json.dumps({
                "image": base64.b64encode(cv2.imencode('.jpg', image)[1]).decode()
            })
        except Exception as e:
            DetectBookController.logger.error(f"Error during detecting book: {e}.")

    def dump_image(self, image, path):
        with open(path, "wb") as file:
            file.write(image)

    def find_book_coordinates(self, book_id: str, objects: list):

        for obj in objects:
            if obj["id"] == book_id:
                return obj["coordinates"]
        return None

    def convert_image(self, image: str):
        return base64.b64decode(image.encode('ascii'))

    def draw_coordinates(self, image_path: str, book_coordinates):
        image = ImageManager.load_image(image_path)
        x1 = book_coordinates["x1"]
        y1 = book_coordinates["y1"]
        x2 = book_coordinates["x2"]
        y2 = book_coordinates["y2"]
        cv2.rectangle(image, (x1, y1), (x2, y2), (250, 137, 73), 7)
        return image
