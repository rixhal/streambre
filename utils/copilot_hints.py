# Hinweise für GitHub Copilot (Streambre Projekt)
"""
Dieses Modul liefert Copilot relevante Kontextinformationen zur Architektur, Struktur und Prioritäten des Projekts.

Copilot kann diese Hinweise verwenden, um konsistente Ergänzungen, neue Module oder Funktionen zu generieren.

Verwendete Quellen und Tools:
- AniWorld.to (Scraping)
- Real-Debrid (Streaming via Magnet-Links)
- XStream+ Struktur als Vorlage
- Torrentio / stremio-addon-sdk (Inspiration)
- BeautifulSoup & Requests (für Scraper)
- Stremio Manifest Standard
"""

project_goals = {
    "ziel": "Ein deutsches Stremio Addon für Anime & Serienstreams",
    "priorität": ["deutsche Quellen", "Dub vor Sub", "ENG nur als Fallback"],
    "services": ["AniWorld.to", "XStream+", "Real-Debrid"],
    "struktur": {
        "scraper": "Für Seiten wie AniWorld und XStream",
        "router": "Routing für Katalog, Suche, Streams",
        "utils": "Hilfsmodule (z.B. Sprache filtern, Formatierer)",
        "manifest.json": "Stremio Manifest mit Suche, Stream-Zugriff und Katalog-Definition"
    },
    "stremio_features": ["search", "catalog", "stream"],
    "sprachfilter": "Priorisiere GER-DUB > GER-SUB > ENG",
    "debrid": "Falls Real-Debrid aktiv: nutze magnet->stream als Fallback",
    "user_focus": "Zielgruppe ist die deutschsprachige Streaming-Community",
    "quellen": [
        "https://aniworld.to",
        "https://www.real-debrid.com/api",
        "https://github.com/phoenixthrush/AniWorld-Downloader",
        "https://github.com/BoredLama/stremio-addon-sdk",
        "https://github.com/Torrentio/streaming-addon-template"
    ]
}

if __name__ == "__main__":
    for k, v in project_goals.items():
        print(f"{k.upper()}: {v}")
