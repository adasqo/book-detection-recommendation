
from bs4 import BeautifulSoup
from requests import Session

class ServiceResponse:

    def __init__(self, session: Session) -> None:
        self.session = session

    def get(self, url: str):
        headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit 537.36 (KHTML, like Gecko) Chrome", "Accept":"text/html,application/xhtml+xml,application/xml; q=0.9,image/webp,*/*;q=0.8"} 
        return self.session.get(url, headers=headers)

    def convert_response_to_list(self, response):
        return BeautifulSoup(response.text, 'html.parser').prettify().split('\n')