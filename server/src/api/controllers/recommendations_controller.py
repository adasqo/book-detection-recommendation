
from src.main.controller.recommendations import RecommendationsController

def get_recommendations(body: dict):  # noqa: E501
    try:
        response = RecommendationsController().get_recommendations(
            body.get("image"), 
            body.get("id"), 
            body.get("lang"))
        return {"status": 200, "response": response}
    except Exception as e:
        return {"status": 400}

