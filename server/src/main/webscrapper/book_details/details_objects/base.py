from bs4 import BeautifulSoup

from abc import ABC, abstractmethod

from src.main.webscrapper.html_parser.base import HTMLParserStrategy

class DetailsObject:

    name: str
    value: str
    parser_strategy: HTMLParserStrategy

    def __init__(self, name: str, parser_strategy: HTMLParserStrategy) -> None:
        self.name = name
        self.parser_strategy = parser_strategy

    @abstractmethod
    def find_value(self):
        self.value = self.parser_strategy.find_element()
        return self.value
