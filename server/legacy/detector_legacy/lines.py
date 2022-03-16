from typing import List
import cv2
import numpy as np

from src.objects.point import Point
from src.objects.line import Line

class LinesDetector:
        
    def detect_lines(self, image: np.array) -> np.array:

        return self.__convert_lines(
            cv2.HoughLinesP(
            image,                  # Input edge image
            1,                      # Distance resolution in pixels
            np.pi/360,              # Angle resolution in radians
            threshold=100,           # Min number of votes for valid line
            minLineLength=25,        # Min allowed length of line
            maxLineGap=1            # Max allowed gap between line for joining them
            )
        )

    def __convert_lines(self, lines_input):
        lines: List[Line] = []
        for line_input in lines_input:
            x_min, y_min, x_max, y_max = line_input[0]
            lines.append(
                Line(
                    Point(x=x_min, y=y_min),
                    Point(x=x_max, y=y_max)
                )
            )
        return lines
