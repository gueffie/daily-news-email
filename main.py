import requests
import glob
from send_email import send_mail

api_key = "83764cd42aae49cebe9281475c360f04"

url = ("https://newsapi.org/v2/everything?q=tesla&from="
       "2024-03-22&sortBy="
       "publishedAt&apiKey=83764cd42aae49cebe9281475c360f04")


request = requests.get(url)
content = request.json()

body: str = ""
for article in content["articles"]:
    if article["description"] and article['title'] is not None:
        body = body + article["title"] + "\n" + article['description'] + 2*"\n"

body = body.encode("utf-8")
send_mail(body)










