import time
from generator import generate_recipe
from nutrition import get_nutrition_data
from substitutions import suggest_substitutes
from utils.sanitizer import sanitize_ingredients
from utils.allergy_checker import check_allergies
from meal_planner import plan_meals
from saver_recipe import save_to_text, save_to_pdf
from shopping_list import generate_shopping_list
from schema_generator import generate_schema

print("👨‍🍳 Welcome to Recipe Generator CLI")

# 🌿 User Input
ingredients_input = input("Enter ingredients (comma separated): ").strip()
diet_pref = input("Any dietary preference (e.g., veg, vegan, keto) [optional]: ").strip()
cuisine = input("Preferred cuisine style (e.g., Indian, Italian, Chinese) [optional]: ").strip()
difficulty = input("Choose difficulty level (easy / medium / hard) [default is medium]: ").strip().lower()
if difficulty not in ["easy", "medium", "hard"]:
    difficulty = "medium"

servings_input = input("How many servings? (default is 1): ").strip()
allergies = input("Any known allergies? (comma separated) [optional]: ").strip().lower()
want_meal_plan = input("Do you want a 3-day meal plan? (yes/no): ").strip().lower()

# 🧮 Validate Servings
try:
    servings = int(servings_input) if servings_input else 1
except ValueError:
    servings = 1

# 🧹 Clean Ingredients
ingredient_list = [i.strip() for i in ingredients_input.split(',') if i.strip()]
sanitized_ingredients = sanitize_ingredients(ingredient_list)

# ⚠️ Allergy Warning
if allergies:
    allergy_list = [a.strip().lower() for a in allergies.split(',')]
    warnings = check_allergies(sanitized_ingredients, allergy_list)
    if warnings:
        print("\n⚠️ Allergy Warning:")
        for w in warnings:
            print(f"- {w}")

# 🔁 Substitutions
print("\n🔄 Suggested Ingredient Substitutes:")
for ing in sanitized_ingredients:
    subs = suggest_substitutes(ing)
    if subs:
        print(f"{ing.title()} → {', '.join(subs)}")

# 📅 Meal Plan
if want_meal_plan == "yes":
    print("\n📅 Generating 3-Day Meal Plan...")
    meal_plan = plan_meals(sanitized_ingredients, diet_pref, cuisine)
    for day, meals in meal_plan.items():
        print(f"\n🗓️ {day}")
        for meal, recipe in meals.items():
            print(f"\n🍽️ {meal}:\n{recipe}")
else:
    # 🍽️ Single Recipe
    print("\n🍽️  Recipe Generated:\n")
    recipe = generate_recipe(sanitized_ingredients, diet_pref, cuisine, servings, difficulty)
    if not recipe:
        print("❌ Error: No recipe generated.")
    else:
        print(recipe)

        # 🧪 Nutrition
        print("\n🧪  Calculating Nutritional Information...\n")
        time.sleep(1)

        total_calories = total_protein = total_carbs = total_fats = 0

        for item in sanitized_ingredients:
            data = get_nutrition_data(item)
            if "foods" in data:
                for food in data["foods"]:
                    cal = food['nf_calories'] * servings
                    prot = food['nf_protein'] * servings
                    carb = food['nf_total_carbohydrate'] * servings
                    fat = food['nf_total_fat'] * servings

                    print(f"\n🔍 {food['food_name'].title()} (x{servings})")
                    print(f"Calories: {round(cal, 2)} kcal")
                    print(f"Protein: {round(prot, 2)} g")
                    print(f"Carbs: {round(carb, 2)} g")
                    print(f"Fats: {round(fat, 2)} g")

                    total_calories += cal
                    total_protein += prot
                    total_carbs += carb
                    total_fats += fat
            else:
                print(f"❌ Error processing '{item}': {data.get('error', 'Unknown error')}")

        # 📊 Summary
        print("\n📊 Total Nutrition Summary (approx.):")
        print(f"🔥 Calories: {round(total_calories, 2)} kcal")
        print(f"💪 Protein: {round(total_protein, 2)} g")
        print(f"🍞 Carbs: {round(total_carbs, 2)} g")
        print(f"🧈 Fats: {round(total_fats, 2)} g")

        # 💾 Save Recipe
        save = input("\n💾 Do you want to save the recipe? (yes/no): ").strip().lower()
        if save == "yes":
            file_format = input("Save as text or PDF? (txt/pdf): ").strip().lower()
            filename = input("Enter filename (without extension): ").strip()

            if file_format == "txt":
                save_to_text(f"{filename}.txt", recipe)
            elif file_format == "pdf":
                save_to_pdf(f"{filename}.pdf", recipe)
            else:
                print("❌ Invalid format. Skipping save.")

        # 🛒 Shopping List
        print("\n🛒 Generating Shopping List...")
        shopping_list = generate_shopping_list(recipe)
        if shopping_list:
            print("\n🧾 Shopping List:")
            for item in shopping_list:
                print(f"- {item}")
        else:
            print("❌ No ingredients found for shopping list.")

    # 🧩 Schema Export
export_schema = input("\n🧩 Do you want to export this recipe in schema format? (yes/no): ").strip().lower()
if export_schema == "yes":
    try:
        filename = input("Enter a filename to save the schema (without .json): ").strip()

        recipe_name = recipe.split("\n")[0].strip("1234567890. *")
        prep_time = 15
        cook_time = 30

        ingredients_start = recipe.find("**Ingredients**:") + len("**Ingredients**:")
        instructions_start = recipe.find("**Instructions**:")
        ingredients_block = recipe[ingredients_start:instructions_start].strip()
        ingredients_list = [line.strip("-• ").strip() for line in ingredients_block.split("\n") if line.strip()]

        instructions_block = recipe[instructions_start:].split("**Serving**")[0]
        instruction_lines = [line for line in instructions_block.split("\n") if line.strip().startswith(tuple("1234567890"))]

        nutrition_data = {
            "calories": total_calories,
            "protein": total_protein,
            "carbs": total_carbs,
            "fats": total_fats
        }

        generate_schema(
            recipe_name=recipe_name,
            cuisine=cuisine,
            servings=servings,
            prep_time=prep_time,
            cook_time=cook_time,
            ingredients=ingredients_list,
            instructions=instruction_lines,
            nutrition_data=nutrition_data,
            filename=filename
        )
    except Exception as e:
        print(f"❌ Schema export failed: {str(e)}")
