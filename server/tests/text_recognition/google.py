import cv2
from google.cloud import vision
import io
import os
from server.src.main.ocr.GoogleOCRModel import GoogleOCRModel
from server.src.main.utils.image_manager import ImageManager

os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="/Users/adam.karwowski/Desktop/google-cred-ocr.json"
    
image_path = "./server/tests/images/test1.jpg"

img = ImageManager.load_image(image_path)

image = None
with io.open(image_path, 'rb') as image_file:
    image = image_file.read()

ocr_model = GoogleOCRModel(
    client = vision.ImageAnnotatorClient())

texts_response = ocr_model.recognize_text(
    image = vision.Image(content=image))

for text in texts_response:
    x1, y1, x2, y2 = text.rectangle.return_coordinates()

    cv2.line(img, (x1, y1), (x1, y2), (0, 255, 0), 2)
    cv2.line(img, (x1, y2), (x2, y2), (0, 255, 0), 2)
    cv2.line(img, (x2, y2), (x2, y1), (0, 255, 0), 2)
    cv2.line(img, (x2, y1), (x1, y1), (0, 255, 0), 2)  
cv2.imshow("Output", img)
cv2.waitKey(0)