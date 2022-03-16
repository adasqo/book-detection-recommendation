from typing import Dict, List
import ssl
from src.main.objects.book import Book
from src.main.objects.text import Text
from src.main.objects.rectangle import Rectangle
ssl._create_default_https_context = ssl._create_unverified_context

class BooksDetector:

    def detect_books(self, books_candidates: List[Rectangle], texts_response: List[Text]):
        
        books: dict = {}
        for text in texts_response:

            book_bounding_box = self.text_has_candidate(text, books_candidates)
            
            if book_bounding_box is None:
                continue

            key = book_bounding_box.__str__()
            if key not in books.keys():
                books[key] = {
                    "texts": [],
                    "rectangle": book_bounding_box
                }
            
            books[key]["texts"].append(text.content)

        return self.create_book_list(books)

    def text_has_candidate(self, text: Text, books_candidates: List[Rectangle]):

        for books_candidate in books_candidates:

            if self.text_in_rectangle(text, books_candidate):
                return books_candidate

        return None

    def text_in_rectangle(self, text: Text, rectangle: Rectangle):

        x1, y1, x2, y2 = text.rectangle.return_coordinates()
        x1r, y1r, x2r, y2r = rectangle.return_coordinates()

        if x1 < x1r or y1 < y1r or x2 > x2r or y2 > y2r:
            return False
        
        return True

    def create_book_list(self, books_dict: dict):

        books = []
        for item in books_dict.values():
            try:
                books.append(
                    Book.build(
                        book_name=" ".join(item["texts"]),
                        rectangle=item["rectangle"])
                    )
            except Exception as err:
                print(" ".join(item["texts"]), err)
                pass
        return books


