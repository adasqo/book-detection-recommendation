

from typing import List
from src.main.webscrapper.response.base import ServiceResponse
from src.main.webscrapper.html_parser.base import HTMLParserStrategy


class GoogleResponse(ServiceResponse):

    service_name: str = "https://www.google.pl"
    parser_strategy: List[HTMLParserStrategy]

    def __init__(self, parser_strategy: HTMLParserStrategy, session) -> None:
        super().__init__(session)
        self.parser_strategy = parser_strategy

    def get_top_link(self, book_name: str, book_service_name: str):
        response = super().get(self.build_url(book_name + f" {book_service_name}"))
        response = super().convert_response_to_list(response)
        return self.__find_top_link(response, f"https://{book_service_name}.pl/ksiazka")

    def build_url(self, book_service_name: str):
        return self.service_name + "/search?q=" + book_service_name

    def __find_top_link(self, response, book_service_name):
        for line in response:
            if book_service_name in line:
                for parser_startegy in self.parser_strategy: 
                    try:
                        return parser_startegy.find_element(line)
                    except:
                        pass
        return None
