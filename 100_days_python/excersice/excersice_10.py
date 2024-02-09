# Exercise 10 Use the NewsAPI and the requests module to fetch the daily news related to different topics.
# Go to: https://newsapi.org/ and explore the various options to build you application

import requests
import json

query = input("What type of news are yu intrested in? ")
url = f"https://newsapi.org/v2/everything?q={query}&from=2024-01-09&sortBy=publishedAt&apiKey=8bf10188bcd34e8d9323dcc373845fb7"
r = requests.get(url)
news  = json.loads(r.text)
print(news, type(news))

for article in news['articles']:
    print(article["title"])
    print(article["description"])
    print("------------------########---------------")