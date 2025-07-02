import requests
from flask import jsonify

def search_aniworld(query):
    print("search_aniworld wurde aufgerufen mit:", query)
    url = "https://aniworld.to/ajax/search"
    headers = {
        "User-Agent": "Mozilla/5.0",
        "X-Requested-With": "XMLHttpRequest",
        "Referer": "https://aniworld.to/search"
    }
    data = {"keyword": query}
    response = requests.post(url, headers=headers, data=data)
    print("Status Code:", response.status_code)
    print("Antwort:", response.text)
    response.raise_for_status()
    results = []
    for entry in response.json():
        print("DEBUG LINK:", entry["link"])
        if entry["link"].startswith("/anime/stream/"):
            results.append({
                "title": entry["title"],
                "url": f'https://aniworld.to{entry["link"]}',
                "description": entry.get("description", "")
            })
    return results  # NICHT jsonify(results)
