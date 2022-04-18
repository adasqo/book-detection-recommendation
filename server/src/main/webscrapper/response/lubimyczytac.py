from src.main.webscrapper.response.base import ServiceResponse


class LubimyCzytacResponse(ServiceResponse):

    def __init__(self, session) -> None:
        super().__init__(session)

    def get(self, url):
        return super().get(url)
