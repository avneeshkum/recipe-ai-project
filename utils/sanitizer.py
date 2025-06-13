# utils/sanitizer.py

def sanitize_ingredient(ingredient):
    mapping = {
        "aloo": "potato",
        "paneer": "paneer",
        "ghee": "ghee",
        "aata": "whole wheat flour",
        "matar": "peas",
        "pyaz": "onion",
        "lahsun": "garlic",
        "dhania": "coriander",
        "mirch": "chili",
        "haldi": "turmeric",
        "jeera": "cumin seeds",
        "adrak": "ginger",
        "patta gobhi":"cabbage",
        "namak":"salt",

    }
    return mapping.get(ingredient.strip().lower(), ingredient.strip().lower())


def sanitize_ingredients(ingredient_list):
    return [sanitize_ingredient(item) for item in ingredient_list]
