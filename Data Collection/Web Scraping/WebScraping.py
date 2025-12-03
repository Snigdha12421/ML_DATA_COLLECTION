import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://books.toscrape.com/"
response = requests.get(url)


if response.status_code != 200:
    print("Failed to retrieve page")
    exit()


soup = BeautifulSoup(response.text, "html.parser")

books = soup.find_all("article", class_="product_pod")

titles = []
prices = []

for book in books:
    title = book.h3.a["title"]
    price = book.find("p", class_="price_color").text

    titles.append(title)
    prices.append(price)

df = pd.DataFrame({
    "Title": titles,
    "Price": prices
})

print("------ Scraped Data from Website ------")
print(df)
