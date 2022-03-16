from dataclasses import dataclass

@dataclass
class Point:

    x: int
    y: int

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def return_coordinates(self):
        return self.x, self.y

    def __str__(self):
        return f"({self.x}, {self.y})"