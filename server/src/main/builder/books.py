# from typing import List
# import uuid
# from src.main.objects.book import Book
# from src.main.objects.rectangle import Rectangle
# from src.main.webscrapper.book_details.details_objects.object_types import DetailsObjectTypes
# # from src.main.webscrapper.book_details.lubimyczytac.lubimyczytac import LubimyCzytacBookDetails
# from src.main.webscrapper.book_details.goodreads.goodreads import GoodReadsBookDetails
# from src.main.webscrapper.html_parser.beautiful_soup import BeautifulSoupBuilder
# from src.main.webscrapper.response.base import ServiceResponse
# from src.main.webscrapper.html_parser.strategies.ref_by_tag import RefByTagStrategy
# import src.main
# from src.main.webscrapper.response.google import GoogleResponse
# # import src.main.webscrapper.book_details.lubimyczytac.properties as properties
# import src.main.webscrapper.book_details.goodreads.properties as properties


# class BooksBuilder:

#     service_name: str = "https://www.google.pl"

#     def __init__(self, session) -> None:
#         self.session = session

#     def build_book(self, book_name: str, rectangle: Rectangle):

#         google_service = GoogleResponse(
#             parser_strategy=[
#                 RefByTagStrategy("href"),
#                 RefByTagStrategy("data-lpage")],
#             session=self.session)

#         book_link = google_service.get_top_link(
#             book_name=book_name,
#             book_service_name=properties.book_service_name)

#         response = ServiceResponse(self.session).get(book_link)

#         details = GoodReadsBookDetails(
#             BeautifulSoupBuilder.build(response)
#         ).find_details()

#         return Book(
#             id=str(uuid.uuid1()),
#             rectangle=rectangle,
#             title=details.get(DetailsObjectTypes.TITLE.value),
#             author=details.get(DetailsObjectTypes.AUTHOR.value),
#             rating=details.get(DetailsObjectTypes.RATING.value),
#             description=details.get(DetailsObjectTypes.DESCRIPTION.value)
#         )

#     def build_books(self, books: dict): 

#         results: List[Book] = []
#         for book in books.values():
#             results.append(
#                 self.build_book(
#                     book_name=" ".join(book["texts"]),
#                     rectangle=book["rectangle"]
#                     ))
#         return results

       