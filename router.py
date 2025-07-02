from flask import Flask, request, jsonify, send_file
import os
from scraper.aniworld import search_aniworld
from utils.language_filter import filter_by_language

app = Flask(__name__)

@app.after_request
def add_ngrok_header(response):
    response.headers["ngrok-skip-browser-warning"] = "true"
    return response

@app.route("/catalog/series/streambre.catalog/search=<query>")
def catalog(query):
    results = search_aniworld(query)
    filtered = filter_by_language(results)
    return jsonify(filtered)

@app.route("/manifest.json")
def manifest():
    return send_file(os.path.join(os.path.dirname(__file__), "manifest.json"))

# Weitere Endpunkte für /stream etc. können ergänzt werden

if __name__ == "__main__":
    app.run(port=7000)