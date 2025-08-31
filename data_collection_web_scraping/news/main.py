import requests
from bs4 import BeautifulSoup

news_url = "https://www.bbc.com/news/world/africa"

response = requests.get(news_url)


soup = BeautifulSoup(response.text, "html.parser")

headlines =  soup.find_all("h2")
links = soup.find_all("a")

with open("./news.txt", "w", encoding="utf-8") as f:
    f.write("H2 Headlines:\n")
    for headline in headlines:
        if text := headline.get_text(strip=True):
            f.write(f"{text}\n")
    f.write("\nA Tag Texts:\n")
    for link in links:
        if text := link.get_text(strip=True):
            f.write(f"{text}\n")
    