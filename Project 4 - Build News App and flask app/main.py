import requests # pip install requests

query = input("What type of news you interested today to Read? => ")
api = "1781c6e459db41b9b808fb6d7ac47231"

url = f"https://newsapi.org/v2/everything?q={query}&from=2025-04-24&sortBy=publishedAt&apiKey={api}"

print(url)
r = requests.get(url)

data = r.json()
articles = data["articles"]

for index, article in enumerate(articles):
    print(index + 1 , article["title"])
    print(article["url"])
    print("\n*************************************\n")