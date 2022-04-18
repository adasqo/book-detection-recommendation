import cv2 
import pytesseract
import cv2
from pytesseract import Output

img = cv2.imread('./server/tests/images/test3.jpg')
img = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


d = pytesseract.image_to_data(gray, output_type=Output.DICT)
print(d)
n_boxes = len(d['level'])
for i in range(n_boxes):
    (x, y, w, h) = (d['left'][i], d['top'][i], d['width'][i], d['height'][i])
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

img = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
cv2.imshow('img', img)
cv2.waitKey(0)