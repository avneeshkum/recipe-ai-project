# schema_generator.py

import json
from datetime import timedelta

def generate_iso_duration(minutes):
    return f"PT{int(minutes)}M"

def generate_schema(recipe_name, cuisine, servings, prep_time, cook_time, ingredients, instructions, nutrition_data, filename):
    schema = {
        "@context": "https://schema.org/",
        "@type": "Recipe",
        "name": recipe_name,
        "recipeCuisine": cuisine if cuisine else "General",
        "recipeCategory": "Main course",
        "recipeYield": f"{servings} servings",
        "prepTime": generate_iso_duration(prep_time),
        "cookTime": generate_iso_duration(cook_time),
        "totalTime": generate_iso_duration(prep_time + cook_time),
        "recipeIngredient": ingredients,
        "recipeInstructions": [
            {"@type": "HowToStep", "text": step.strip()} for step in instructions
        ],
        "nutrition": {
            "@type": "NutritionInformation",
            "calories": f"{round(nutrition_data['calories'], 2)} kcal",
            "proteinContent": f"{round(nutrition_data['protein'], 2)} g",
            "carbohydrateContent": f"{round(nutrition_data['carbs'], 2)} g",
            "fatContent": f"{round(nutrition_data['fats'], 2)} g"
        }
    }

    with open(f"sample_recipes/schemas/{filename}.json", "w") as f:
        json.dump(schema, f, indent=4)

    print(f"\n✅ Recipe Schema saved as sample_recipes/schemas/{filename}.json")
