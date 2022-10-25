import requests

has_next = True
next_cursor = "1:0:0"

while has_next:
    params = {
        "limit": "50",
        "thread": "9413338442",
        "forum": "breitbartproduction",
        "order": "popular",
        "cursor": next_cursor,
        "api_key": "E8Uh5l5fHZ6gD8U3KycjAIAk46f68Zw7C6eW8WSjZvCLXebZ7p0r1yrYDrLilk2F",
    }

    r = requests.get(
        "https://disqus.com/api/3.0/threads/listPostsThreaded",
        params=params,
    )
    r = r.json()


    comments = r["response"]
    for c in comments:
        print(c["raw_message"].strip())

    has_next = r["cursor"]["hasNext"]
    next_cursor = r["cursor"]["next"]
