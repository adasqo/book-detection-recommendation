from typing import List

from src.database.task_status import TaskStatus
from src.main.objects.book import Book
from src.main.ocr.GoogleOCRModel import GoogleOCRModel
from src.main.detector.book_candidates import BooksCandidatesDetector
from src.main.detector.book import BooksDetector
from src.main.utils.image_manager import ImageManager
from src.database.client import ElasticsearchClient

import cv2
from google.cloud import vision
import base64
import json
import logging

class RecommendationsController:

    logger = logging.getLogger()

    def __init__(self) -> None:
        self.elastic_client = ElasticsearchClient()

    def get_recommendations(self, image: str, task_id: str, lang: str):

        RecommendationsController.logger.info("Get recommendations request started.")

        self.elastic_client.create_task(task_id)

        image_path = f"./images/{task_id}.jpg"

        image = self.convert_image(image)

        self.dump_image(image, image_path)

        ocr_model = GoogleOCRModel(client=vision.ImageAnnotatorClient())

        texts_response = ocr_model.recognize_text(image=vision.Image(content=image))

        RecommendationsController.logger.info("Text recognition step finished.")

        books_cadidates = BooksCandidatesDetector().detect_books_candidates(image_path)

        RecommendationsController.logger.info("Object detection step finished.")

        books: List[Book] = BooksDetector(lang).detect_books(books_cadidates, texts_response)

        RecommendationsController.logger.info("Books detection step finished.")

        self.save_results(self.elastic_client, task_id, image_path, books)

        results = self.prepare_results(image_path, books)

        self.elastic_client.close()

        return results

    def convert_image(self, image: str):
        return base64.b64decode(image.encode('ascii'))

    def dump_image(self, image, path):
        with open(path, "wb") as file:
            file.write(image)

    def save_results(self, elastic_client: ElasticsearchClient, task_id: str, image_path: str, books: List[Book]):
        results = []
        for book in books:
            x1, y1, x2, y2 = book.rectangle.return_coordinates()
            details = {
                "id": book.id,
                "title": book.title,
                "author": book.author,
                "rating": book.rating,
                "description": book.description,
                "coordinates": {
                    "x1": x1,
                    "y1": y1,
                    "x2": x2,
                    "y2": y2
                }
            }
            results.append(details)

        result_json = {
            "image": base64.b64encode(
                cv2.imencode('.jpg', ImageManager.load_image(image_path))[1]).decode(),
            "books": results
        }

        elastic_client.update_task(task_id, result_json, TaskStatus.FINISHED.value)

    def prepare_results(self, image_path: str, books: List[Book]):
        image = ImageManager.load_image(image_path)
        results = []
        for book in books:
            x1, y1, x2, y2 = book.rectangle.return_coordinates()
            cv2.rectangle(image, (x1, y1), (x2, y2), (250, 137, 73), 5)
            details = {
                "id": book.id,
                "title": book.title,
                "author": book.author,
                "rating": book.rating,
                "description": book.description
            }
            results.append(details)

        return json.dumps({
            "image": base64.b64encode(cv2.imencode('.jpg', image)[1]).decode(),
            "books": results
        })
