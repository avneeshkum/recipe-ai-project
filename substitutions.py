substitution_map = {
    "ghee": ["olive oil", "coconut oil"],
    "paneer": ["tofu", "tempeh"],
    "potato": ["sweet potato", "turnip"],
    "onion": ["leek", "shallot"],
    "garlic": ["asafoetida (hing)", "ginger"],
    "peas": ["edamame", "green beans"],
    "tomato": ["red bell pepper puree", "pumpkin puree"],
    "butter": ["olive oil", "avocado"],
    "cream": ["yogurt", "cashew cream"],
    "milk": ["almond milk", "soy milk"]
}

def suggest_substitutes(ingredient):
    lower_ingredient = ingredient.lower()
    return substitution_map.get(lower_ingredient, [])
