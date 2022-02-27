from dataclasses import dataclass

from src.objects.point import Point

@dataclass
class Line:

    point1: Point
    point2: Point

    def __init__(self, point1: Point, point2: Point):
        self.point1 = point1
        self.point2 = point2

    def return_coordinates(self):
        return self.point1.x, self.point1.y, self.point2.x, self.point2.y

    def return_x_sum(self):
        return self.point1.x + self.point2.x

    def return_x_difference(self):
        return self.point1.x - self.point2.x

    def return_y_sum(self):
        return self.point1.y + self.point2.y

    def return_y_difference(self):
        return self.point1.y - self.point2.y
