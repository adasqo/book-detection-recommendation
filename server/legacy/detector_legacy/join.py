from cmath import pi
from typing import List
import cv2
import numpy as np
from src.objects.point import Point

from src.objects.line import Line

class JoinLines:

    def __init__(self) -> None:

        self.epsilon_a = 5 * pi / 180
        self.epsilon_b = 10

        self.lower_range = 0
        self.upper_range = 10000
        
    def join_lines(self, lines_input: List[Line]):

        lines_output: List[Line] = []
        lines_seen: List[Line] = []
        for line in lines_input:

            if line in lines_seen:
                continue
            
            lines_join = self.__get_collinear_lines(line, lines_input)
            lines_output.append(self.__join_lines(lines_join))
            lines_seen.extend(lines_join)   

        return self.__filter_close_lines(lines_output)

    def __get_collinear_lines(self, line: Line, lines_input: List[Line]):
        
        lines_output: List[Line] = []
        
        for line_input in lines_input:
            if self.__check_lines_collinearity(line, line_input):
                lines_output.append(line_input)

        return lines_output 

    def __check_lines_collinearity(self, line1: Line, line2: Line):

        x11, y11, x12, y12 = line1.return_coordinates()
        x21, y21, x22, y22 = line2.return_coordinates()

        vector1 = [x11 - x12, y11 - y12]
        vector2 = [x11 - x21, y11 - y21]
        vector3 = [x11 - x22, y11 - y22]

        cross_product1 = np.cross(vector1, vector2)
        cross_product2 = np.cross(vector1, vector3)

        area1 = np.linalg.norm(cross_product1)
        area2 = np.linalg.norm(cross_product2)

        if area1 < 100 and area2 < 100:
            return True
        return False

    def __join_lines(self, lines: List[Line]):

        x_max = -1
        x_min = 10000
        y_max = -1
        y_min = 10000

        for line in lines:

            x1, y1, x2, y2 = line.return_coordinates()

            if x1 < x_min:
                x_min = x1
            if x2 > x_max:
                x_max = x2
            if y1 > y_max:
                y_max = y1
            if y2 < y_min:
                y_min = y2

        return Line(
            Point(x_min, y_min),
            Point(x_max, y_max))

    def __filter_close_lines(self, lines_input: List[Line]):

        lines_input = sorted(lines_input, key=lambda line: line.point1.x)
        _iter = 0
        while True:
            try:
                line = lines_input[_iter]
            except IndexError:
                break
            left_line = self.__find_closest_line_in_diraction("left", line, lines_input)
            result_left = self.__merge_lines(left_line, line)
            if len(result_left) == 1:
                _iter_prev = _iter
                if left_line in lines_input:
                    lines_input.remove(left_line)
                    _iter += 1
                if line in lines_input:
                    lines_input.remove(line)
                    _iter += 1
                lines_input.extend(result_left)
                if _iter - _iter_prev == 2:
                    _iter = _iter_prev
                lines_input = sorted(lines_input, key=lambda line: line.point1.x)
            else:
                _iter += 1
            
        return lines_input

    def __find_closest_line_in_diraction(self, direction, line_org: Line, lines: List[Line]):
        
        x = int(line_org.return_x_sum() / 2)

        while self.__check_direction_condition(direction, x):

            for line in lines:
                if line == line_org:
                    continue

                x_line = int(line.return_x_sum() / 2)

                if x_line == x:
                    return line

            x = self.__change_x_value(direction, x)

        return None

    def __check_direction_condition(self, direction, x):
        if direction == "left":
            return x >= self.lower_range
        if direction == "right":
            return x <= self.upper_range
        return False

    def __change_x_value(self, direction, x):
        if direction == "left":
            return x - 1
        if direction == "right":
            return x + 1
        return x

    def __merge_lines(self, line1: Line, line2: Line):
        
        if line1 is None and line2 is not None:
            return [line2]
        if line2 is None and line1 is not None:
            return [line1]

        _, y11, _, y21 = line1.return_coordinates()
        _, y12, _, y22 = line2.return_coordinates()

        x1 = int(line1.return_x_sum() / 2)
        x2 = int(line2.return_x_sum()/ 2)

        if abs(x1 - x2) < 15:
            return [
                Line(
                    Point(int((x1 + x2) / 2), int((y11 + y12) / 2)), 
                    Point(int((x1 + x2) / 2), int((y21 + y22) / 2))
                )
            ]
        return [line1, line2]

