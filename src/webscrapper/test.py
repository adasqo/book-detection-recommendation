# import requests

# def googleSearch(query):
#     with requests.session() as c:
#         url = 'https://www.google.com/'
#         # query = {'q': query}
#         response = requests.get(url, params = {'q': query})
#         # print(response)
#         # print(response.content) # Return the raw bytes of the data payload
#         # print(response.text) # Return a string representation of the data payload
#         print(response.text) # This method is convenient when the API returns JSON

# googleSearch('Gra o tron lubimyczytac')

import requests
import urllib
# import pandas as pd
from requests_html import HTML
from requests_html import HTMLSession

def get_source(url):
    """Return the source code for the provided URL. 

    Args: 
        url (string): URL of the page to scrape.

    Returns:
        response (object): HTTP response object from requests_html. 
    """

    try:
        session = HTMLSession()
        response = session.get(url)
        return response

    except requests.exceptions.RequestException as e:
        print(e)

def scrape_google(query):

    query = urllib.parse.quote_plus(query)
    response = get_source("https://www.google.pl/search?q=" + query)

    links = list(response.html.absolute_links)

    links_return = []
    for url in links[:]:
        if url.startswith("https://lubimyczytac.pl/"):
            links_return.append(url)

    return links_return

links = scrape_google("gra o tron lubimyczytac")
# print(links)




# response = get_source("https://lubimyczytac.pl/ksiazka/32296/gra-o-tron")

# print(response.content)

import json
import requests

r = requests.get('https://lubimyczytac.pl/ksiazka/32296/gra-o-tron', stream=True)

for line in r.iter_lines():

    # filter out keep-alive new lines
    if line:
        line = line.decode("utf-8") 
        if "name=\"title\" content=" in line:
            print(line)
        if "</span> / 10" in line:
            print(line)


