from dataclasses import dataclass
from src.main.objects.rectangle import Rectangle

from src.main.objects.text import Text
from src.main.webscrapper.response.google import GoogleResponse
from src.main.webscrapper.html_parser.strategies.ref_by_tag import RefByTagStrategy
from src.main.webscrapper.html_parser.beautiful_soup import BeautifulSoupBuilder
import src.main.webscrapper.lubimyczytac.properties as properties
from src.main.webscrapper.book_details.lubimyczytac import LubimyCzytacBookDetails
from src.main.webscrapper.response.lubimyczytac import LubimyCzytacResponse
from src.main.webscrapper.book_details.details_objects.object_types import DetailsObjectTypes

@dataclass
class Book:

    rectangle: Rectangle
    title: str
    author: str
    rating: str
    description: str

    def __init__(self, rectangle: Rectangle, title: str, author: str, rating: str, description: str):
        self.rectangle = rectangle
        self.title = title
        self.author = author
        self.rating = rating
        self.description = description

    @staticmethod
    def build(book_name: str, rectangle: Rectangle):

        google_service = GoogleResponse(
            parser_strategy=[
                RefByTagStrategy("href"),
                RefByTagStrategy("data-lpage")  
            ])

        book_link = google_service.get_top_link(
            book_name=book_name,
            book_service_name=properties.book_service_name)

        response = LubimyCzytacResponse().get(book_link)

        details = LubimyCzytacBookDetails(
            BeautifulSoupBuilder.build(response)
        ).find_details()

        return Book(
            rectangle=rectangle,
            title=details.get(DetailsObjectTypes.TITLE.value),
            author=details.get(DetailsObjectTypes.AUTHOR.value),
            rating=details.get(DetailsObjectTypes.RATING.value),
            description=details.get(DetailsObjectTypes.DESCRIPTION.value)
        )

    def __str__(self):
        return f"Title: \"{self.title}\", author: {self.author}, rating {self.rating}, coordinates: {self.rectangle.__str__()}"
