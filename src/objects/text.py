from src.objects.point import Point
from typing import Tuple
from dataclasses import dataclass

@dataclass
class Text:

    content: str
    origin: Point
    width: int
    height: int

    def __init__(self, content: str, origin: Point, width: int, height: int):
        self.content = content
        self.origin = origin
        self.width = width
        self.height = height
