# utils/allergy_checker.py

# Allergy mapping: common allergens with possible related ingredients
ALLERGY_MAP = {
    "dairy": ["milk", "cheese", "butter", "cream", "yogurt", "paneer", "ghee", "curd"],
    "nuts": ["almond", "peanut", "cashew", "walnut", "hazelnut", "pistachio"],
    "gluten": ["wheat", "barley", "rye", "flour", "bread", "pasta"],
    "soy": ["soy", "soya", "tofu", "soybean"],
    "egg": ["egg", "eggs", "egg white", "egg yolk"],
    "seafood": ["fish", "shrimp", "prawn", "crab", "lobster"],
    "sesame": ["sesame", "tahini"],
    "mustard": ["mustard", "mustard oil"],
    "shellfish": ["shrimp", "crab", "lobster", "scallop", "oyster"],
}

def check_allergies(ingredients, allergies):
    flagged = []
    allergies = [a.lower().strip() for a in allergies]

    for item in ingredients:
        item_lower = item.lower()
        for allergy in allergies:
            related_items = ALLERGY_MAP.get(allergy, [allergy])
            if any(rel in item_lower for rel in related_items):
                flagged.append(f"{item} (related to {allergy})")
                break
    return flagged
