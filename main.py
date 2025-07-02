"""
Streambre Main Launcher
"""
import sys
from scraper.aniworld import search_aniworld

def main():
    """
    Führt eine Suche auf Aniworld mit dem angegebenen Suchbegriff aus und gibt die Ergebnisse aus.
    """
    if len(sys.argv) < 2:
        print("Usage: python main.py <search_term>")
        sys.exit(1)
    search_term = " ".join(sys.argv[1:])  # Erlaubt Suchbegriffe mit mehreren Wörtern
    try:
        results = search_aniworld(search_term)
        if not results:
            print("Keine Ergebnisse gefunden.")
            return
        print(f"Ergebnisse für '{search_term}':")
        for idx, r in enumerate(results, 1):
            print(f"{idx}. {r}")
    except Exception as e:
        print(f"Fehler bei der Suche: {e}")
        sys.exit(2)

if __name__ == "__main__":
    main()
