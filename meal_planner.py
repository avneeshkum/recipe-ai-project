# meal_planner.py
import random
from generator import generate_recipe

def plan_meals(ingredients_list, dietary_pref, cuisine, days=3):
    plan = {}
    for day in range(1, days + 1):
        plan[f"Day {day}"] = {
            "Breakfast": generate_recipe(random.sample(ingredients_list, min(3, len(ingredients_list))), dietary_pref, cuisine, 1),
            "Lunch": generate_recipe(random.sample(ingredients_list, min(4, len(ingredients_list))), dietary_pref, cuisine, 2),
            "Dinner": generate_recipe(random.sample(ingredients_list, min(5, len(ingredients_list))), dietary_pref, cuisine, 2)
        }
    return plan
