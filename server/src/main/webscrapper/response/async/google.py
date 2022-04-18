

# from typing import List
# from src.main.webscrapper.response.base import ServiceResponse
# from src.main.webscrapper.html_parser.base import HTMLParserStrategy

# import asyncio
# import time 
# import aiohttp
# from aiohttp.client import ClientSession

# async def hello(url):
#     async with ClientSession(connector=aiohttp.TCPConnector()) as session:
#         async with session.get(url, ssl=False, headers=headers) as response:
#             response = await response.read()
#             print(response)

# class GoogleResponse(ServiceResponse):

#     service_name: str = "https://www.google.pl"
#     parser_strategy: List[HTMLParserStrategy]

#     def __init__(self, parser_strategy: HTMLParserStrategy, session) -> None:
#         super().__init__(session)
#         self.parser_strategy = parser_strategy

#     def get_top_link(self, book_name: str, book_service_name: str):
#         response = super().get(self.__build_url(book_name + f" {book_service_name}"))
#         response = super().convert_response_to_list(response)
#         return self.__find_top_link(response, f"https://{book_service_name}.pl/ksiazka")

#     def __build_url(self, book_service_name: str):
#         return self.service_name + "/search?q=" + book_service_name + "&num=0"

#     def __find_top_link(self, response, book_service_name):
#         for line in response:
#             if book_service_name in line:
#                 for parser_startegy in self.parser_strategy: 
#                     try:
#                         return parser_startegy.find_element(line)
#                     except:
#                         pass
#         return None