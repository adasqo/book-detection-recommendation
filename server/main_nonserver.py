
from typing import List
from src.main.objects.rectangle import Rectangle
from src.main.objects.point import Point
from src.main.objects.book import Book
from src.main.detector.book import BooksDetector
from src.main.detector.book_candidates import BooksCandidatesDetector
from src.main.ocr.GoogleOCRModel import GoogleOCRModel
import cv2
from src.main.utils.image_manager import ImageManager
from google.cloud import vision
import io
import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="/Users/adam.karwowski/Desktop/google-cred-ocr.json"

if __name__ == "__main__":
    
    image_path = "test_images/test13.jpg"

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
    
    #     cv2.line(img, (x1, y1), (x1, y2), (255, 255, 0), 2)
    #     cv2.line(img, (x1, y2), (x2, y2), (255, 255, 0), 2)
    #     cv2.line(img, (x2, y2), (x2, y1), (255, 255, 0), 2)
    #     cv2.line(img, (x2, y1), (x1, y1), (255, 255, 0), 2)  
    # cv2.imshow("Output", img)
    # cv2.waitKey(0)

    books_cadidates = BooksCandidatesDetector().detect_books_candidates(image_path)

    # for book in books_cadidates:
    #     x1, y1, x2, y2 = book.return_coordinates()
    
    #     cv2.line(img, (x1, y1), (x1, y2), (255, 255, 0), 2)
    #     cv2.line(img, (x1, y2), (x2, y2), (255, 255, 0), 2)
    #     cv2.line(img, (x2, y2), (x2, y1), (255, 255, 0), 2)
    #     cv2.line(img, (x2, y1), (x1, y1), (255, 255, 0), 2)  
    # cv2.imshow("Output", img)
    # cv2.waitKey(0)

    img = ImageManager.load_image(image_path)

    books: List[Book] = BooksDetector().detect_books(books_cadidates, texts_response)
   
    for book in books:
        x1, y1, x2, y2 = book.rectangle.return_coordinates()
        print(book)
    
        cv2.line(img, (x1, y1), (x1, y2), (255, 255, 0), 2)
        cv2.line(img, (x1, y2), (x2, y2), (255, 255, 0), 2)
        cv2.line(img, (x2, y2), (x2, y1), (255, 255, 0), 2)
        cv2.line(img, (x2, y1), (x1, y1), (255, 255, 0), 2)  
    cv2.imshow("Output", img)
    cv2.waitKey(0)
