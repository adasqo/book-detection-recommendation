from src.main.controller.detect_book import DetectBookController

def detect_book(body: dict):  # noqa: E501
    try:
        response = DetectBookController().detect_book(body.get("task_id"), body.get("book_id"), )
        return {"status": 200, "response": response}
    except Exception:
        return {"status": 400}
