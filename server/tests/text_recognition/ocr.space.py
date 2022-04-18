import io
import json
import cv2
import numpy as np
import requests

file_name = "./server/tests/images/test3.jpg"
img = cv2.imread(file_name)
img = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)
height, width, _ = img.shape
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

url_api = "http://api.ocr.space/parse/image"
_, compressedimage = cv2.imencode(".jpg", gray, [1, 90])
file_bytes = io.BytesIO(compressedimage)

result = requests.post(
    url_api,
    files = {file_name: file_bytes},
    data = { 
        "apikey": "K81408595588957", 
        "language": "pol",
        "isOverlayRequired": True
        })

result = result.content.decode()
result = json.loads(result)

res = result.get("ParsedResults")[0].get("TextOverlay").get("Lines")
# text_detected = parsed_results.get("ParsedText")
# print(result)
# boxes = text_detected.get("TextOverlay").get("Lines")

for r in res:
    words = r.get("Words")
    for word in words:
        (x, y, w, h) = (word.get('Left'), word.get("Top"), word.get("Width"), word.get("Height"))
        cv2.rectangle(img, (int(x), int(y)), (int(x + w), int(y + h)), (0, 255, 0), 2)

img = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
cv2.imshow('img', img)
cv2.waitKey(0)