import asyncio
from time import time
from typing import List
import uuid

from bs4 import BeautifulSoup
from src.main.webscrapper.html_parser.base import HTMLParserStrategy
from src.main.objects.book import Book
from src.main.webscrapper.book_details.details_objects.object_types import DetailsObjectTypes
from src.main.webscrapper.book_details.lubimyczytac.lubimyczytac import LubimyCzytacBookDetails
from src.main.webscrapper.book_details.goodreads.goodreads import GoodReadsBookDetails
import src.main.webscrapper.book_details.lubimyczytac.properties as lubimyczytac_properties
import src.main.webscrapper.book_details.goodreads.properties as goodreads_properties
import aiohttp
from aiohttp.client import ClientSession


class BooksBuilderAsync:

    def __init__(self, parser_strategy: List[HTMLParserStrategy], lang: str) -> None:
        self.parser_strategy = parser_strategy
        self.lang = lang
        self.service_name: str = "https://www.google.pl" if lang == "pl" else "https://www.google.com"
        self.book_service_name = lubimyczytac_properties.book_service_name if lang == "pl" else goodreads_properties.book_service_name

    @staticmethod
    async def get_response(url: str, headers: bool = True):
        _headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit 537.36 (KHTML, like Gecko) Chrome", "Accept":"text/html,application/xhtml+xml,application/xml; q=0.9,image/webp,*/*;q=0.8"}
       
        async with ClientSession(connector=aiohttp.TCPConnector()) as session:
            if headers:
                async with session.get(
                        url,
                        ssl=False, 
                        headers=_headers) as response:
                    return await response.read()
            else:
                 async with session.get(
                        url,
                        ssl=False) as response:
                    return await response.read()
                
    def get_responses_google(self, books: dict):

        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        tasks = []
        for book in books.values():
            task = asyncio.ensure_future(
                BooksBuilderAsync.get_response(
                    self.service_name + "/search?q=" + " ".join(book["texts"]) + f" {self.book_service_name}", 
                    ))
            tasks.append(task)
        responses = loop.run_until_complete(asyncio.gather(*tasks))
        return responses

    def find_top_link(self, response):
        scheme = f"https://{self.book_service_name}.pl/ksiazka" if self.lang == "pl" else f"https://www.{self.book_service_name}.com/book/show"
        for line in response:
            if scheme in line:
                for parser_startegy in self.parser_strategy: 
                    try:
                        return parser_startegy.find_element(line)
                    except:
                        pass
        return None

    def get_top_links(self, responses: list):

        top_links = []
        for response in responses:
            resp = BeautifulSoup(response, 'html.parser').prettify().split('\n')
            top_links.append(self.find_top_link(resp))
        return top_links

    def get_responses_book(self, top_links: list):

        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        tasks = []
        for link in top_links:
            task = asyncio.ensure_future(
                BooksBuilderAsync.get_response(link, headers=False))
            tasks.append(task)
        responses = loop.run_until_complete(asyncio.gather(*tasks))
        return responses

    def create_books(self, responses_books, rectangles):

        results = []
        for i in range(len(responses_books)):
            parser = BeautifulSoup(responses_books[i], 'html.parser')
            book_details = LubimyCzytacBookDetails(parser) if self.lang == "pl" else GoodReadsBookDetails(parser)
            details = book_details.find_details()

            results.append(Book(
                id=str(uuid.uuid1()),
                rectangle=rectangles[i],
                title=details.get(DetailsObjectTypes.TITLE.value),
                author=details.get(DetailsObjectTypes.AUTHOR.value),
                rating=details.get(DetailsObjectTypes.RATING.value),
                description=details.get(DetailsObjectTypes.DESCRIPTION.value)
            ))
        return results

    def __eliminate_empty_links(self, responses: list, links: list, texts: list):

        responses_return = []
        links_return = []
        texts_return = []
        for i in range(len(links)):
            if links[i] is None:
                continue
            responses_return.append(responses[i])
            links_return.append(links[i])
            texts_return.append(texts[i])
        return responses_return, links_return, texts_return

    def build_books(self, books: dict): 

        rectangles = [book["rectangle"] for book in books.values()]
        _time = time()
        responses = self.get_responses_google(books)
        top_links = self.get_top_links(responses)
        responses, top_links, rectangles = self.__eliminate_empty_links(responses, top_links, rectangles)
        responses_books = self.get_responses_book(top_links)
        print(time() - _time)
        books = self.create_books(responses_books, rectangles)
        return books
       