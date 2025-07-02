import requests
from bs4 import BeautifulSoup

def search_aniworld(query):
    url = f"https://aniworld.to/anime-search?search={query}"
    headers = {
        "User-Agent": "Mozilla/5.0"
    }
    resp = requests.get(url, headers=headers, timeout=10)
    soup = BeautifulSoup(resp.text, "lxml")
    results = []
    for entry in soup.select(".anime-entry"):
        title = entry.select_one(".anime-title").get_text(strip=True)
        link = entry.select_one("a")["href"]
        poster = entry.select_one("img")["src"]
        results.append({
            "id": link.split("/")[-1],
            "type": "series",
            "name": title,
            "poster": poster,
            "description": "",  # Optional: Scrape Beschreibung auf Detailseite
            "genres": []        # Optional: Scrape Genres auf Detailseite
        })
    return results

def get_popular_aniworld():
    url = "https://aniworld.to/"
    headers = {"User-Agent": "Mozilla/5.0"}
    resp = requests.get(url, headers=headers, timeout=10)
    soup = BeautifulSoup(resp.text, "lxml")
    results = []
    for entry in soup.select(".top-anime .anime-entry"):
        title = entry.select_one(".anime-title").get_text(strip=True)
        link = entry.select_one("a")["href"]
        poster = entry.select_one("img")["src"]
        results.append({
            "id": link.split("/")[-1],
            "type": "series",
            "name": title,
            "poster": poster,
            "description": "",
            "genres": []
        })
    return results
