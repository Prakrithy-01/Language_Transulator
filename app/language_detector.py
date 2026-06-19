from langdetect import detect

def detect_language(text):

    lang = detect(text)

    mapping = {
        "en": "english",
        "hi": "hindi",
        "ml": "malayalam",
        "ta": "tamil",
        "fr": "french",
        "ar": "arabic",
        "ko": "korean",
        "bn": "bengali",
        "ur": "urdu",
        "ru": "russian",
    }

    return mapping.get(lang, "english")