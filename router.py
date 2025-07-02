from flask import Flask, request, jsonify, send_file
import os
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Dummy-Scraper für Demo-Zwecke
def search_aniworld(query):
    # Hier später echten Scraper einbinden!
    # Beispiel-Daten:
    return [
        {
            "id": "aniworld-001",
            "type": "series",
            "name": f"Demo Anime zu '{query}'",
            "poster": "https://aniworld.to/img/demo.jpg",
            "description": "Demo-Beschreibung",
            "genres": ["Action", "Abenteuer"]
        }
    ]

@app.route("/catalog/series/streambre.catalog/search=<query>")
def catalog(query):
    results = search_aniworld(query)
    return jsonify(results)

@app.route("/catalog/series/streambre.catalog.json")
def catalog_no_search():
    # Gib eine Liste von Beispiel-Serien zurück
    return jsonify([
        {
            "id": "aniworld-001",
            "type": "series",
            "name": "Demo Anime 1",
            "poster": "https://aniworld.to/img/demo.jpg",
            "description": "Demo-Beschreibung",
            "genres": ["Action", "Abenteuer"]
        },
        {
            "id": "aniworld-002",
            "type": "series",
            "name": "Demo Anime 2",
            "poster": "https://aniworld.to/img/demo2.jpg",
            "description": "Noch ein Demo",
            "genres": ["Comedy"]
        }
    ])

@app.route("/manifest.json")
def manifest():
    return send_file(os.path.join(os.path.dirname(__file__), "manifest.json"))

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)