from src.main.objects.rectangle import Rectangle
from dataclasses import dataclass

@dataclass
class Text:

    content: str
    rectangle: Rectangle

    def __init__(self, content: str, rectangle: Rectangle):
        self.content = content
        self.rectangle = rectangle
