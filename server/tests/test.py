# from src.webscrapper.response.google import GoogleResponse
# from src.webscrapper.html_parser.strategies.href import HrefStrategy
# from src.webscrapper.html_parser.beautiful_soup import BeautifulSoupBuilder
# import src.webscrapper.lubimyczytac.properties as properties
# from src.webscrapper.book_details.lubimyczytac import LubimyCzytacBookDetails
# from src.webscrapper.response.lubimyczytac import LubimyCzytacResponse

# google_service = GoogleResponse(
#     parser_strategy=HrefStrategy()
# )

# book_link = google_service.get_top_link(
#     book_name="Gra o tron",
#     book_service_name=properties.book_service_name)

# response = LubimyCzytacResponse().get(book_link)

# LubimyCzytacBookDetails(
#     BeautifulSoupBuilder.build(response)
# ).find_details()
