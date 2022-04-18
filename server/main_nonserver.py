
from time import time
from typing import List

import cv2
from google.cloud import vision
import io
import os
from src.main.models_utils.detection_model import BooksDetectionModel
from src.main.detector.book_candidates import BooksCandidatesDetector
from src.main.ocr.GoogleOCRModel import GoogleOCRModel
from src.main.utils.image_manager import ImageManager
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="/Users/adam.karwowski/Desktop/google-cred-ocr.json"

if __name__ == "__main__":
    
    image_path = "./server/tests/images/test3.jpg"

    img = ImageManager.load_image(image_path)

    image = None
    with io.open(image_path, 'rb') as image_file:
        image = image_file.read()

    ocr_model = GoogleOCRModel(
        client = vision.ImageAnnotatorClient())

    texts_response = ocr_model.recognize_text(
        image = vision.Image(content=image))

    # for text in texts_response:
    #     x1, y1, x2, y2 = text.rectangle.return_coordinates()
    
    #     cv2.line(img, (x1, y1), (x1, y2), (0, 255, 0), 2)
    #     cv2.line(img, (x1, y2), (x2, y2), (0, 255, 0), 2)
    #     cv2.line(img, (x2, y2), (x2, y1), (0, 255, 0), 2)
    #     cv2.line(img, (x2, y1), (x1, y1), (0, 255, 0), 2)  
    # cv2.imshow("Output", img)
    # cv2.waitKey(0)
    BooksDetectionModel.initiate_detection_model()

    _time = time()
    books_cadidates = BooksCandidatesDetector().detect_books_candidates(image_path)
    print(time() - _time)
    for book in books_cadidates:
        x1, y1, x2, y2 = book.return_coordinates()
    
        cv2.line(img, (x1, y1), (x1, y2), (255, 255, 0), 2)
        cv2.line(img, (x1, y2), (x2, y2), (255, 255, 0), 2)
        cv2.line(img, (x2, y2), (x2, y1), (255, 255, 0), 2)
        cv2.line(img, (x2, y1), (x1, y1), (255, 255, 0), 2)  
    cv2.imshow("Output", img)
    cv2.waitKey(0)

    # img = ImageManager.load_image(image_path)

    # books: List[Book] = BooksDetector().detect_books(books_cadidates, texts_response)
   
    # for book in books:
    #     x1, y1, x2, y2 = book.rectangle.return_coordinates()
    #     print(book)
    
    #     cv2.line(img, (x1, y1), (x1, y2), (255, 255, 0), 2)
    #     cv2.line(img, (x1, y2), (x2, y2), (255, 255, 0), 2)
    #     cv2.line(img, (x2, y2), (x2, y1), (255, 255, 0), 2)
    #     cv2.line(img, (x2, y1), (x1, y1), (255, 255, 0), 2)  
    # cv2.imshow("Output", img)
    # cv2.waitKey(0)
