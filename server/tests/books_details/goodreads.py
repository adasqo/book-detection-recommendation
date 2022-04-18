from bs4 import BeautifulSoup
import requests

url = "https://www.goodreads.com/book/show/13496.A_Game_of_Thrones"

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
res = soup.prettify()
# print(res)
# with open("goodreads.txt", "w") as file:
#     file.write(res)

#id="bookTitle"
#class="authorName"
#itemprop="ratingValue"
#id="description"
title = soup.find(attrs={"id" : "description"}).get_text().strip()
print(title)