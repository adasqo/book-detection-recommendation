

from src.main.webscrapper.response.base import ServiceResponse
from src.main.webscrapper.html_parser.base import HTMLParserStrategy


class LubimyCzytacResponse(ServiceResponse):

    def __init__(self) -> None:
        super().__init__()

    def get(self, url):
        return super().get(url)
