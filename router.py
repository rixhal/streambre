from flask import Flask, request, jsonify, send_file
import os
from flask_cors import CORS
from scraper.aniworld import search_aniworld, get_popular_aniworld
import random
import string

app = Flask(__name__)
CORS(app)

@app.route("/catalog/series/streambre.catalog/search=<query>")
def catalog(query):
    results = search_aniworld(query)
    return jsonify({"metas": results})

@app.route("/catalog/series/streambre.catalog.json")
def catalog_no_search():
    try:
        results = get_popular_aniworld()
    except Exception as e:
        results = []
    return jsonify({"metas": results})

@app.route("/manifest.json")
def manifest():
    return send_file(os.path.join(os.path.dirname(__file__), "manifest.json"))

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)