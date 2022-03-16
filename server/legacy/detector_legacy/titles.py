
from typing import Dict, List
from unittest import result
from src.objects.point import Point
from src.objects.line import Line
from src.objects.text import Text


class TextDetector:

    def __init__(self) -> None:
        self.lower_range = 0
        self.upper_range = 10000
        self.epsilon = 10

    def remove_covering_lines(self, texts: List[Text], lines_input: List[Line], img):

        lines_output: List[Line] = []
        for line in lines_input:
            if self.__determine_if_line_in_text_boundries(line, texts):
                continue
            lines_output.append(line)
        return lines_output

    def __determine_if_line_in_text_boundries(self, line: Line, texts: List[Text]):

        x_line = int(line.return_x_sum() / 2)
        for text in texts:
            x_text, _ = text.origin.return_coordinates()
            width_text = text.width
            if x_text - int(width_text / 2) + self.epsilon < x_line and \
                x_line < x_text + int(width_text / 2) - self.epsilon:
                return True
        return False

    def detect_text(self, texts: List[Text], lines: List[Line]):

        clusters = {}
        for text in texts:
            results = self.__get_closest_lines(text, lines)
            left, right = results

            self.__add_text_to_cluster(clusters, text, left, right)

        clusters = self.__determine_bounding_boxes_of_cluster(clusters)
        
        return clusters

    def __get_closest_lines(self, text: Text, lines: List[Line]):
    
        left_line = self.__find_closest_line_in_diraction("left", text, lines)
        right_line = self.__find_closest_line_in_diraction("right", text, lines)

        return left_line, right_line

    def __find_closest_line_in_diraction(self, direction, text: Text, lines: List[Line]):
        
        x_text = text.origin.x
        x = x_text

        line = None
        
        while self.__check_direction_condition(direction, x):

            for line in lines:
                x_line = int((line.return_x_sum()) / 2)

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

    def __add_text_to_cluster(self, clusters: Dict[str, List[Text]], text, left, right):
        key = '(' + str(left) + ', ' + str(right) + ')'
        if key not in clusters.keys():
            clusters[key] = []
        clusters[key].append(text)

    def __determine_bounding_boxes_of_cluster(self, clusters: Dict[str, List[Text]]):

        results = []
        for texts in clusters.values():
            results.append({
                "texts": [text.content for text in texts],
                "coordinates": self.__get_cluster_coordinates(texts)
            })
                
            print([text.content for text in texts])
        return results

    def __get_cluster_coordinates(self, texts: List[Text]):

        box_coordinates = self.__initiate_box_coordinates()

        for text in texts:
            box_coordinates = self.__update_box_coordinates(text, box_coordinates)
        
        return self.__increase_box_bounrdies(box_coordinates)

    def __initiate_box_coordinates(self):
        return 10000, 10000, 0, 0
            

    def __update_box_coordinates(self, text: Text, box_coordinates):

        x1, y1, x2, y2 = self.__unpack_text_coordinates(text)
        x1_c, y1_c, x2_c, y2_c = box_coordinates
        
        if x1 < x1_c:
            x1_c = x1
        if y1 < y1_c:
            y1_c = y1
        if x2 > x2_c:
            x2_c = x2
        if y2 > y2_c:
            y2_c = y2

        return x1_c, y1_c, x2_c, y2_c

    def __unpack_text_coordinates(self, text: Text):
        x, y = text.origin.return_coordinates()
        x1 = x - int(text.width / 2)
        y1 = y - int(text.height / 2)
        x2 = x + int(text.width / 2)
        y2 = y + int(text.height / 2)
        return x1, y1, x2, y2

    def __increase_box_bounrdies(self, box_coordinates):
        x1_c, y1_c, x2_c, y2_c = box_coordinates
        eps = 0
        return x1_c - eps, y1_c - eps, x2_c + eps, y2_c + eps