from bs4 import BeautifulSoup

from src.main.webscrapper.html_parser.base import HTMLParserStrategy


class ValueBySelectorStrategy(HTMLParserStrategy):

    def __init__(self, parser: BeautifulSoup, selector_key: str, selector_value: str) -> None:
        self.parser = parser
        self.selector_key = selector_key
        self.selector_value = selector_value

    def find_element(self):
        return self.parser.find(attrs={self.selector_key : self.selector_value}).get_text().strip()