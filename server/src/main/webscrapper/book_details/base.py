from typing import List
from bs4 import BeautifulSoup
from src.main.webscrapper.book_details.details_objects.base import DetailsObject

class BookDetails:

    title: DetailsObject
    author: DetailsObject
    rating: DetailsObject
    description: DetailsObject

    def __init__(self, title: DetailsObject, author: DetailsObject, rating: DetailsObject, description: DetailsObject) -> None:

        self.title = title
        self.author = author
        self.rating = rating
        self.description = description
        
        self.details_objects: List[DetailsObject] = [
            self.title, self.author, self.rating, self.description
        ]

    def find_details(self):

        details = {}
        for detials_object in self.details_objects:
            try:
                details[detials_object.name]=detials_object.find_value()
            except:
                pass
        return details
        