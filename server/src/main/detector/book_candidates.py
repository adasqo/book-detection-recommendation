from src.main.objects.point import Point
from src.main.objects.rectangle import Rectangle
from src.main.models_utils.detection_model import BooksDetectionModel


class BooksCandidatesDetector:

    def __init__(self) -> None:
        self.model = BooksDetectionModel.get_model()

    def detect_books_candidates(self, image_path: str):
        
        results = []
        objects = self.model(image_path)

        objects = objects.pandas().xyxy[0]

        for i in range(len(objects)):

            _object = objects.iloc[i]

            if _object["name"] != "book":
                continue

            x1 = _object["xmin"]
            y1 = _object["ymin"]
            x2 = _object["xmax"]
            y2 = _object["ymax"]

            results.append(
                Rectangle(
                    origin=Point(int((x1 + x2) / 2), int((y1 + y2) / 2)),
                    width=int(abs(x1 - x2)),
                    height=int(abs(y1 - y2))
                )
            )
        return results



