from time import time
from typing import Dict, List
import ssl
import logging

from requests import Session
from src.main.webscrapper.html_parser.strategies.ref_by_tag import RefByTagStrategy
from src.main.builder.books_async import BooksBuilderAsync
# from src.main.builder.books import BooksBuilder
# from src.main.objects.book import Book
from src.main.objects.text import Text
from src.main.objects.rectangle import Rectangle
ssl._create_default_https_context = ssl._create_unverified_context
import asyncio

class BooksDetector:

    logger = logging.getLogger()

    def __init__(self, lang: str) -> None:
        self.lang = lang

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
        return BooksBuilderAsync(
            parser_strategy=[
                RefByTagStrategy("href"),
                RefByTagStrategy("data-lpage")],
            lang=self.lang
        ).build_books(books_dict)
