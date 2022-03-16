from requests_html import HTMLSession
from bs4 import BeautifulSoup

class ServiceResponse:

    def __init__(self) -> None:
        self.session = HTMLSession()

    def get(self, url: str):
        return self.session.get(url)

    def convert_response_to_list(self, response):
        return BeautifulSoup(response.text, 'html.parser').prettify().split('\n')