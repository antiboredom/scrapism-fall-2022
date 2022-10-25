import requests
import time

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:106.0) Gecko/20100101 Firefox/106.0",
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "Accept-Language": "en-US,en;q=0.5",
    # 'Accept-Encoding': 'gzip, deflate, br',
    "Origin": "https://soundcloud.com",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-site",
    "Authorization": "OAuth 2-293494-57384203-16heCzshhLrslIb",
    "Referer": "https://soundcloud.com/",
    "Connection": "keep-alive",
    "Pragma": "no-cache",
    "Cache-Control": "no-cache",
}

offset = 0

while offset < 1000:
    params = {
        "client_id": "1TLciEOiKE0PThutYu5Xj0kc8R4twD9p",
        "offset": offset,
        "threaded": "1",
        "limit": "20",
        "app_version": "1666362116",
        "app_locale": "en",
    }

    response = requests.get(
        "https://api-v2.soundcloud.com/tracks/24880470/comments",
        params=params,
        headers=headers,
    )
    data = response.json()

    comments = data["collection"]
    for c in comments:
        print(c["body"])

    offset = offset + 20
    time.sleep(0.1)
