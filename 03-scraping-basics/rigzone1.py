import requests
from bs4 import BeautifulSoup
import time

for page in range(1, 453):
    url = "https://www.rigzone.com/oil/jobs/search/?page=" + str(page)
    # print(url)
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    jobs = soup.select(".description")
    for j in jobs:
        print(j.text.strip())

    time.sleep(0.5)
