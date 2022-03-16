from bs4 import BeautifulSoup

class BeautifulSoupBuilder:

    @staticmethod
    def build(response):
        return BeautifulSoup(response.text, "html.parser")