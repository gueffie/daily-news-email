import requests
import glob
from send_email import send_mail

topic = "tesla"
api_key = "83764cd42aae49cebe9281475c360f04"

url = ("https://newsapi.org/v2/everything?"
       f"q={topic}&"
       "from=2024-03-22&"
       "sortBy=publishedAt&"
       "apiKey=83764cd42aae49cebe9281475c360f04&"
       "language=en")


request = requests.get(url)
content = request.json()

body: str = "Subject: Today's news" + "\n"

for article in content["articles"][:20]:
    if article["description"] and article['title'] and ['url'] is not None:
        body = body + article["title"] + "\n" \
               + article['description'] + "\n" \
               + article["url"] + 2*"\n"


body = body.encode("utf-8")
send_mail(body)










