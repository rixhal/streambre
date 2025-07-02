import requests
from bs4 import BeautifulSoup

BASE_URL = "https://aniworld.to"
HEADERS = {"User-Agent": "Mozilla/5.0"}

def search_aniworld(query):
    print(f"🔎 Suche: {query}")
    res = requests.get(f"{BASE_URL}/suche/{query.replace(' ', '+')}", headers=HEADERS)
    soup = BeautifulSoup(res.text, "html.parser")
    entries = soup.select(".film-series")
    links = []

    for item in entries:
        try:
            title = item.select_one("a")["title"]
            href = BASE_URL + item.select_one("a")["href"]
            lang = item.select_one(".language").text.strip().lower()
            if "ger-dub" in lang or "ger sub" in lang:
                links.append({"title": title, "url": href, "lang": lang})
        except:
            continue

    return links
