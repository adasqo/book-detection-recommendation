from cmath import pi
from typing import List
import cv2

from src.objects.line import Line

class AngledLinesDetector:

    def __init__(self, angle: int) -> None:
        self.angle = angle
        self.epsilon = 15 * pi / 180
        
    def detect_lines(self, lines_input: List[Line]):

        lines_output: List[Line] = []
        for line in lines_input:

            angle = self.__get_line_angle(line)
            if abs(angle - self.angle) < self.epsilon:
                lines_output.append(line)

        return lines_output

    def __get_line_angle(self, line: Line):

        if abs(line.return_x_difference()) < self.epsilon:
            return pi / 2

        return line.return_y_difference() / line.return_x_difference()
