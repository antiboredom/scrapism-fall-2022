from requests_html import HTMLSession

session = HTMLSession()

response = session.get("https://newyork.craigslist.org/search/bar")
response.html.render(sleep=2) # you may need to adjust this number!
elements = response.html.find(".post-title .label")
for e in elements:
    print(e.text.strip())
