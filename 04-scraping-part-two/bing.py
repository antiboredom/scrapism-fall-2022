import requests
from bs4 import BeautifulSoup

letters = "abcdefghijklmnopqrstuvwxyz"

for l in letters:
    params = {
        'pt': 'page.home',
        'mkt': 'pt-pt',
        'qry': 'how do i ' + l,
        'asv': '1',
        'cp': '3',
        'msbqf': 'false',
        'cvid': '480BAB86D4BC40BEA3B9984DF29D80CA',
    }

    response = requests.get('https://www.bing.com/AS/Suggestions', params=params)
    soup = BeautifulSoup(response.text, "html.parser")
    items = soup.select("li")
    for i in items:
        print(i.text.strip())
