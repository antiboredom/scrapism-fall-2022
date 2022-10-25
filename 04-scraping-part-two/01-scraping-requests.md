# Scraping Network Requests

Websites will frequently load in multiple stages. In the first stage, some basic HTML/CSS and JavaScript source gets loaded. In the second stage, JavaScript will make additional network requests that retrieve and insert the bulk of the site's content. This loading of extra content using JavaScript is referred to as "AJAX" (Asynchronous JavaScript And XML) or "XHR" (XML HTTP Request).

To scrape sites that use this technique you can use real browsers (we will talk about this later), or you can attempt to detect the network requests being made, and then duplicate those requests directly from the command line or through a script. It can actually be much easier and faster to scrape this way.


## Inspecting Network Requests

To see what network requests your browser is making, first open up your developer tools. In Chrome, from the `View` menu, select `Developer` and then `Developer Tools`. Or, use the keyboard shortcut `command-option-i`.

Then click the `Network` button. You should see a list of all the requests your browser has made for the page you're on. Note that you may need to refresh the page after opening up the `Network` tab to see the requests.

The list should contain the initial HTML page, stylesheets, JavaScript files, images, and possibly much more. Typically this is a bit overwhelming. You can filter the list to only view specific requests by selecting requests types from the top bar.

## Parsing HTML Fragments

As an example, let's look at what happens when you start typing a search query into Bing.com. As is common, every keystroke you type is sent to Bing, which then suggests possible queries based on what others have searched for.

Opening the network inspector and filtering by XHR, you can see the requests being made in real time, listed according to the request URL.

Click on any request to see more details. For example, you can scroll to the bottom of the `Headers` tab to see the query string for the request.

The `Response` tab shows the raw response from the server.

The `Preview` tab provides a useful view, which changes based on the type of file requested. In this case, it is an HTML snippet:

You can copy the URL of the request by right-clicking on it to use later in a Python script.

We can easily duplicate the request in Python using `requests` and `BeautifulSoup`. Note that I have edited the URL to replace the hard-coded query with a variable.

```python
from bs4 import BeautifulSoup
import requests

query = "How can I"
url = (
    "https://www.bing.com/AS/Suggestions?pt=page.home&mkt=en-us&qry="
    + query
    + "&cp=10&cvid=B8D86CB090A240A196E4867715E40B15"
)
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
items = soup.select("li")
for item in items:
    print(item.text)
```

To expand our search and extract more results, we can iterate through the letters of the alphabet in a nested loop, appending letter pairs to our initial base query.

```python
from bs4 import BeautifulSoup
import requests

def auto_complete(query):
  url = (
      "https://www.bing.com/AS/Suggestions?pt=page.home&mkt=en-us&qry="
      + query
      + "&cp=10&cvid=B8D86CB090A240A196E4867715E40B15"
  )
  response = requests.get(url)
  soup = BeautifulSoup(response.text, "html.parser")
  items = soup.select("li")
  for item in items:
      print(item.text)

base_query = "How can I "
for letter in "abcdefghijklmnopqrstuvwxyz":
    auto_complete(base_query + letter)
    for letter2 in "abcdefghijklmnopqrstuvwxyz":
        auto_complete(base_query + letter + letter2)
```

This results in many duplicates. To sort the output of our script and filter out duplicates, you can pipe the script through the `sort -u` command, like so:

```bash
python3 bing_autocomplete.py | sort -u
```

## Scraping JSON

Frequently network requests will return JSON data rather than HTML snippets. JSON, which stands for JavaScript Object Notation, is a plain-text file format for defining data structures with key and value pairs, with a syntax modelled on JavaScript's for defining objects.

A JSON file might look something like this, with an object containing a single key, `people`, whose value is an array of objects.

```json
{
  "people": [
    {
      "firstName": "Karl",
      "lastName": "Marx"
    },
    {
      "firstName": "Franz",
      "lastName": "Kafka"
    }
  ]
}
```

You may have noticed that JSON is structured quite similar to Python's `dictionary` type. In fact, it is easy to transform JSON into Python dictionaries, and vice versa.