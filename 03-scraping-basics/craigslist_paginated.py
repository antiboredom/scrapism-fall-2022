import requests
from bs4 import BeautifulSoup
import time

start = 0

while True:
    url = "https://newyork.craigslist.org/search/bar?s=" + str(start)
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    elements = soup.select(".result-heading")
    if len(elements) == 0:
        break

    for e in elements:
        print(e.text.strip())

    start = start + 120
    time.sleep(0.5)