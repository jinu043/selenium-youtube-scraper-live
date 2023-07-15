youtube_trending_url = "https://www.youtube.com/feed/trending"

import requests
from bs4 import BeautifulSoup

response = requests.get(youtube_trending_url)

with open("trending.html", "w") as f:
  f.write(response.text)

doc = BeautifulSoup(response.text, "html.parser")

print("Page title: ", doc.title)
