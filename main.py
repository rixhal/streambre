"""
Streambre Main Launcher
"""

from scraper.aniworld import search_aniworld

if __name__ == "__main__":
    results = search_aniworld("naruto")
    for r in results:
        print(r)
