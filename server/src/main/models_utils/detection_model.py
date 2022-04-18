import torch
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

class BooksDetectionModel:

    model: None

    @staticmethod
    def initiate_detection_model():
        BooksDetectionModel.model = torch.hub.load('ultralytics/yolov5', 'yolov5l')

    @staticmethod
    def get_model():
        if BooksDetectionModel.model is None:
            BooksDetectionModel.initiate_detection_model()
        return BooksDetectionModel.model
