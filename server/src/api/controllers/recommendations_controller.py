import connexion
import six

from src.api import util
from src.main.controller.recommendations import RecommendationsController

def get_recommendations(image):  # noqa: E501
    """Send image and receive recommendations

     # noqa: E501

    :param image: 
    :type image: werkzeug.datastructures.FileStorage

    :rtype: List[str]
    """
    print(image)
    # print(image.read())
    RecommendationsController.get_recommendations(image.read(), "id")
    return "Success", 200
