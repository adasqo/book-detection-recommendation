# import torch
# import ssl

# from src.detector.book import BookDetector
# ssl._create_default_https_context = ssl._create_unverified_context

# # # Model
# # model = torch.hub.load('ultralytics/yolov5', 'yolov5s')  # or yolov5m, yolov5l, yolov5x, custom

# # # Images
# # img = 'test_images/test3.jpg'  # or file, Path, PIL, OpenCV, numpy, list

# # # Inference
# # results = model(img)

# # # Results
# # results.show()  # or .show(), .save(), .crop(), .pandas(), etc.
# # print(results.pandas())

# image_path = 'test_images/test.jpg'

# detector = BookDetector()
# books_candidates = detector.detect_books(image_path)