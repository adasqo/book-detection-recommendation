from dataclasses import dataclass

from src.main.objects.point import Point

@dataclass
class Rectangle:

    origin: Point
    width: int
    height: int

    def __init__(self, origin: Point, width: int, height: int) -> None:
        self.origin = origin
        self.width = width
        self.height = height

    def __str__(self):
        return f"(Rectangle: {self.origin}, width: {self.width}, height: {self.height})"

    def return_coordinates(self):

        x_c, y_c = self.origin.return_coordinates()
        return x_c - int(self.width / 2), \
                y_c - int(self.height / 2), \
                x_c + int(self.width / 2), \
                y_c + int(self.height / 2)
                