from src.main.webscrapper.html_parser.base import HTMLParserStrategy
import re

class RefByTagStrategy(HTMLParserStrategy):

    tag: str 

    def __init__(self, tag: str) -> None:
        super().__init__()
        self.tag = tag

    def find_element(self, content: str):
        return re.findall(f"{self.tag}=[\"\'](.*?)[\"\']", content)[0]