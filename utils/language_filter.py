def     filter_by_language(results):
    # Ergebnisse nach Sprache priorisieren
    dub = [r for r in results if "Ger Dub" in r["title"]]
    sub = [r for r in results if "Ger Sub" in r["title"]]
    eng = [r for r in results if "Eng" in r["title"]]
    # Wenn keine Sprache gefunden wurde, gib alle zurück
    return dub or sub or eng or results