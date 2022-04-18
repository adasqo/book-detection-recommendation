# from flask import session
from requests_html import HTMLSession
# from requests import Session
from time import time

url = "https://www.google.com/search?q=male+zycie+lubimyczytac.pl"

# html_session = HTMLSession()

# requests_session = Session()

# _time = time()
# r = html_session.get(url)
# print(time() - _time)
# print(r.text)

# _time = time()
# # _ = requests_session.get(url)
# r = requests_session.get(url)
# print(r.text)
# print(time() - _time)

# import aiohttp
# import asyncio
# import requests

# with requests.Session() as session:
#     response = session.get(url)
#     print(response.text)

# import aiohttp
# import asyncio

# async def main():

#     async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(verify_ssl=False)) as session:
#         async with session.get(url) as response:

#             print("Status:", response.status)
#             print("Content-type:", response.headers['content-type'])

#             html = await response.text()
#             print("Body:", html, "...")

# loop = asyncio.get_event_loop()
# loop.run_until_complete(main())

# import requests
# from bs4 import BeautifulSoup
   
# # Enter the City Name
# # city = input("Enter the City Name: ")
# search = "Weather in {}".format("Warsaw")
  
# # URL 
# url = f"http://www.google.com/search?&q={search}" 
   
# # Sending HTTP request
# _time = time()
# req = requests.get(url)
# print(time() - _time)
  
# # Pulling HTTP data from internet
# sor = BeautifulSoup(req.text, "html.parser") 
  
# # Finding temperature in Celsius
# temp = sor.find("div", class_='BNeawe').text
  
# print(temp)

# import faster_than_requests as requests

# _time = time()
# r = requests.get(url)
# print(time() - _time)
# print(r)

headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit 537.36 (KHTML, like Gecko) Chrome", "Accept":"text/html,application/xhtml+xml,application/xml; q=0.9,image/webp,*/*;q=0.8"}


import requests

# session = requests.Session()
# r = session.get(url, headers=headers)
# print(r.text)


import asyncio
import time 
import aiohttp
from aiohttp.client import ClientSession

loop = asyncio.get_event_loop()
async def hello(url):
    async with ClientSession(connector=aiohttp.TCPConnector()) as session:
        async with session.get(url, ssl=False, headers=headers) as response:
            response = await response.read()
            print(response)

tasks = []
for i in range(10):
    task = asyncio.ensure_future(hello(url))
    tasks.append(task)
loop.run_until_complete(asyncio.wait(tasks))

# async def download_link(url:str, session:ClientSession):
#     async with session.get(url) as response:
#         result = await response.text()
#         print(f'Read {len(result)} from {url}')

# async def download_all(urls:list):
#     my_conn = aiohttp.TCPConnector(limit=10)
#     async with aiohttp.ClientSession(connector=my_conn) as session:
#         tasks = []
#         for url in urls:
#             task = asyncio.ensure_future(download_link(url=url,session=session))
#             tasks.append(task)
#         return await asyncio.gather(*tasks,return_exceptions=True) # the await must be nest inside of the session

# url_list = [url]*10
# start = time.time()
# loop = asyncio.get_event_loop()
# loop.run_until_complete(download_all(url_list))
# end = time.time()
# print(f'download {len(url_list)} links in {end - start} seconds')

# import aiohttp
# import asyncio

# headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit 537.36 (KHTML, like Gecko) Chrome", "Accept":"text/html,application/xhtml+xml,application/xml; q=0.9,image/webp,*/*;q=0.8"}
# url += "&ie=utf-8&oe=utf-8"

# async def main():

#     my_conn = aiohttp.TCPConnector()
#     async with aiohttp.ClientSession(connector=my_conn) as session:
#         async with session.get(url, ssl=False, headers=headers) as response:

#             print("Status:", response.status)
#             print("Content-type:", response.headers['content-type'])

#             html = await response.text()
#             print("Body:", html, "...")

# loop = asyncio.get_event_loop()
# loop.run_until_complete(main())

# import aiohttp
# import asyncio

# headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit 537.36 (KHTML, like Gecko) Chrome", "Accept":"text/html,application/xhtml+xml,application/xml; q=0.9,image/webp,*/*;q=0.8"}
# url += "&ie=utf-8&oe=utf-8"

# async def main():
#     async with aiohttp.ClientSession(trust_env=True, connector=aiohttp.TCPConnector()) as session:
#         async with session.get(url, ssl=False, headers=headers) as resp:
#             print(resp.status)
#             print(await resp.text())

# loop = asyncio.get_event_loop()
# loop.run_until_complete(main())



# from urllib.request import Request, urlopen
# reqest = Request(url, headers=headers)
# page = urlopen(reqest)
# print(page)
