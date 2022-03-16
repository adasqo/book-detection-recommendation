from src.main.webscrapper.book_details.base import BookDetails
from src.main.webscrapper.book_details.details_objects.base import DetailsObject
from src.main.webscrapper.book_details.details_objects.object_types import DetailsObjectTypes
from src.main.webscrapper.html_parser.strategies.value_by_selector import ValueBySelectorStrategy
import src.main.webscrapper.lubimyczytac.properties as properties
from bs4 import BeautifulSoup

class LubimyCzytacBookDetails(BookDetails):

    def __init__(self, parser: BeautifulSoup) -> None:
        super().__init__(
            title = DetailsObject(
                name=DetailsObjectTypes.TITLE.value,
                parser_strategy=ValueBySelectorStrategy(
                    parser=parser,
                    selector_key=properties.title_selector_key,
                    selector_value=properties.title_selector_value
                )
            ),
            author = DetailsObject(
                name=DetailsObjectTypes.AUTHOR.value,
                parser_strategy=ValueBySelectorStrategy(
                    parser=parser,
                    selector_key=properties.author_selector_key,
                    selector_value=properties.author_selector_value
                )
            ),
            rating = DetailsObject(
                name=DetailsObjectTypes.RATING.value,
                parser_strategy=ValueBySelectorStrategy(
                    parser=parser,
                    selector_key=properties.rating_selector_key,
                    selector_value=properties.rating_selector_value
                )
            ),
            description = DetailsObject(
                name=DetailsObjectTypes.DESCRIPTION.value,
                parser_strategy=ValueBySelectorStrategy(
                    parser=parser,
                    selector_key=properties.description_selector_key,
                    selector_value=properties.description_selector_value
                )
            )
        )