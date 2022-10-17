import requests
from bs4 import BeautifulSoup

response = requests.get("https://www.nytimes.com/")
# print(response.text)
soup = BeautifulSoup(response.text, "html.parser")
elements = soup.select("h3")
for e in elements:
    print(e.text.strip())