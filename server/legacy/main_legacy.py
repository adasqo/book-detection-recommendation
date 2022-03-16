from cmath import pi
import json
from tkinter import Image
import numpy as np
from src.objects.rectangle import Rectangle
from src.objects.point import Point
from src.objects.book import Book
from src.detector.titles import TextDetector
from src.detector.join import JoinLines
from src.detector.angles import AngledLinesDetector
from src.detector.lines import LinesDetector
from ocr.GoogleOCRModel import GoogleOCRModel
import cv2
from src.utils.image_manager import ImageManager
from google.cloud import vision
import io
import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="/Users/adam.karwowski/Desktop/google-cred-ocr.json"

if __name__ == "__main__":
    
    image_path = "test_images/test.jpg"

    img = ImageManager.load_image(image_path)

    image = None
    with io.open(image_path, 'rb') as image_file:
        image = image_file.read()

    ocr_model = GoogleOCRModel(
        client = vision.ImageAnnotatorClient()
    )
    texts_response = ocr_model.recognize_text(
        image = vision.Image(content=image)
    )

    # for text in texts_response:
    #     content = text.content
    #     x, y = text.origin.return_coordinates()
    #     width = text.width
    #     height = text.height
    #     cv2.rectangle(img, (x - int(width/2), y - int(height/2)), (x + int(width/2), y + int(height/2)), (255, 255, 255), 2)
    #     cv2.putText(img, content, (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
    # cv2.imshow("Output", img)
    # cv2.waitKey(0)


    image_org = ImageManager.load_image(image_path)
    image = ImageManager.convert_to_grayscale(image_org)
    image = ImageManager.blur_image(image, 3)
    image = ImageManager.detect_edges(image, 50, 100)
    
    img = ImageManager.load_image(image_path)
    
    lines = LinesDetector().detect_lines(image)

    lines = AngledLinesDetector(pi / 2).detect_lines(lines)

    lines = JoinLines().join_lines(lines)

    lines = TextDetector().remove_covering_lines(texts_response, lines, img)

    clusters = TextDetector().detect_text(texts_response, lines)
   
    for cluster in clusters:
        coordinates = cluster["coordinates"]
        x1, y1, x2, y2 = coordinates
        try:
            book = Book.build(
                book_name=" ".join(cluster["texts"]),
                rectangle=Rectangle(
                    origin=Point(int((x1 + x2) / 2), int((y1 + y2) / 2)),
                    width=int(abs(x1 - x2) / 2),
                    height=int(abs(y1 - y2) / 2)
                )         
            )
            print(book)
        except:
            pass

        cv2.line(img, (x1, y1), (x1, y2), (255, 255, 0), 2)
        cv2.line(img, (x1, y2), (x2, y2), (255, 255, 0), 2)
        cv2.line(img, (x2, y2), (x2, y1), (255, 255, 0), 2)
        cv2.line(img, (x2, y1), (x1, y1), (255, 255, 0), 2)  
    cv2.imshow("Output", img)
    cv2.waitKey(0)

