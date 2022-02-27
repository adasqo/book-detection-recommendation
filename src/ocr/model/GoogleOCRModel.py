import numpy as np
from typing import Dict, List

from src.objects.text import Text
from src.objects.point import Point

class GoogleConnectionError(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)

class GoogleOCRModel:

    def __init__(self, client):
        self.client = client

    def recognize_text(self, image) -> Dict[str, np.array]:
        """
        Method accapts image (np.array), recognizes text and returns dict
        containing text (str) and its bounding boxes
        """
        response = self.client.text_detection(image=image)

        texts: List[Text] = []
        first_seen = False

        for text_annotation in response.text_annotations:

            if not first_seen:
                first_seen = True
                continue

            texts.append(
                Text(
                    content=text_annotation.description,
                    origin=Point(
                        x=int((text_annotation.bounding_poly.vertices[0].x + text_annotation.bounding_poly.vertices[2].x) / 2), 
                        y=int((text_annotation.bounding_poly.vertices[0].y + text_annotation.bounding_poly.vertices[2].y) / 2)),
                    width=abs(int(text_annotation.bounding_poly.vertices[2].x - text_annotation.bounding_poly.vertices[0].x)),
                    height=abs(int(text_annotation.bounding_poly.vertices[2].y - text_annotation.bounding_poly.vertices[0].y))
                )
            )
        if response.error.message:
            raise GoogleConnectionError('{}\nFor more info on error messages, check: https://cloud.google.com/apis/design/errors'.format(response.error.message))

        return texts
        