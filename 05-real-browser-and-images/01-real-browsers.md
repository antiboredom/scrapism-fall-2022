# Real Browsers

So far we've been using `requests` to download html & json files, and `beautifulsoup` as a parsing tool. I generally suggest using this combo (or something similar) for most web scraping tasks.

Another technique which is useful for avoiding anti-scraping measures, or generally just mimicking human browsing behavior is to automate a real browser like Chrome or Firefox. This tends to be a bit slower than downloading and parsing HTML, but gives you the ability to scrape otherwise-difficult sites, and allows you to do fun things like take screenshots and fill out forms. This means that rather than making an http request with `requests` you actually open up a real browser and control it via a script.

There are at least three libraries for this: selenium, puppeteer and playwright. I like using playwright the most so that's what we'll be using!

Here's a link to the [playwright for python documentation](https://playwright.dev/python/docs/intro).


## Installation

To install `playwright`:

```
pip3 install playwright
playwright install
```

*Note: the `playwright install` command downloads a copy of chrome for you!

## Scrape

Here's a basic scraping task you can do with playwright:

```python
# import the library
from playwright.sync_api import sync_playwright

# set up playwright
p = sync_playwright().start()

# launch a the chrome browser
# you can also launch safari with p.webkit.launch()
# or firefox: p.firefox.launch()
browser = p.chromium.launch(headless=False)

# open up a new empty page
page = browser.new_page()

# have the browser visit lav.io
page.goto("https://lav.io")

# grab all the "a" tags
# use locator(SELECTOR) to grab elements with
# a specific css selector
links = page.locator("a")

# iterate through them and print
# the text and href attribute
for l in links:
    print(l.text_content().strip())
    print(l.get_attribute("href"))
    
# close the browser
browser.close()

# shut down playwright
playwright.stop()
```


## Be a person

You can use playwright to fill out forms with the `page.fill(SELECTOR)` function:

```python
import time
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://google.com")

    page.fill("input.gLFyf", "how do i")
    page.keyboard.press("Enter")

    page.wait_for_timeout(10000)

    browser.close()
```

## Logging in to a website

To come!

## Save a screenshot

To save a screenshot of a website just run:

```
page.screenshot(path="screenshot.png", full_page=True)
```

If `full_page` is set to be `True` it will save the entire page, otherwise it will save just what's visible.

You can also capture a specific element like so (replacing "SELECTOR" with the selector of the element you wish to capture.

```
page.locator("SELECTOR").screenshot(path="screenshot.png")
```

## Calling JavaScript

to come!


