import re

def generate_shopping_list(recipe_text):
    lines = recipe_text.splitlines()
    ingredients_section = False
    ingredients = []

    for line in lines:
        stripped_line = line.strip()

        # Fix: Match markdown bold headings like "**Ingredients**:"
        if not ingredients_section and re.search(r"\*\*ingredients\*\*:", stripped_line, re.IGNORECASE):
            ingredients_section = True
            continue

        # Stop when instructions or any new heading starts
        if ingredients_section:
            if re.search(r"\*\*instructions\*\*:", stripped_line, re.IGNORECASE):
                break

            # Match lines like "- 200g paneer..."
            match = re.match(r"[-•]\s+(.*)", stripped_line)
            if match:
                item = match.group(1).strip()
                if item:
                    ingredients.append(item)

    return ingredients
