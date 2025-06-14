import streamlit as st
import time
import os
from generator import generate_recipe
from nutrition import get_nutrition_data
from substitutions import suggest_substitutes
from utils.sanitizer import sanitize_ingredients
from utils.allergy_checker import check_allergies
from meal_planner import plan_meals
from saver_recipe import save_to_text, save_to_pdf  # ✅ Fixed Import
from shopping_list import generate_shopping_list
from schema_generator import generate_schema

# 🎨 Page Config
st.set_page_config(page_title="Recipe Generator", page_icon="🍽️", layout="wide")

st.title("👨‍🍳 Recipe Generator")

# ✅ Initialize session state to prevent resets
for key in ["recipe", "shopping_list", "schema_file", "sanitized_ingredients", "saved_file", "success_message_txt", "success_message_pdf", "success_message_schema"]:
    if key not in st.session_state:
        st.session_state[key] = None if key != "sanitized_ingredients" else []

# 🌿 User Inputs
ingredients_input = st.text_input("Enter ingredients (comma separated):")
diet_pref = st.selectbox("Dietary preference (optional)", ["None", "Veg", "Vegan", "Keto", "Gluten-Free"])
cuisine = st.selectbox("Preferred cuisine style (optional)", ["None", "Indian", "Italian", "Chinese", "Mexican"])
difficulty = st.radio("Choose difficulty level", ["Easy", "Medium", "Hard"], index=1)
servings = st.number_input("How many servings?", min_value=1, value=1)
allergies = st.text_input("Any known allergies? (comma separated)")
want_meal_plan = st.checkbox("Generate a 3-day meal plan")

# ✅ Generate Recipe (Session State)
if st.button("Generate Recipe"):
    ingredient_list = [i.strip() for i in ingredients_input.split(',') if i.strip()]
    st.session_state.sanitized_ingredients = sanitize_ingredients(ingredient_list)
    st.session_state.recipe = generate_recipe(st.session_state.sanitized_ingredients, diet_pref, cuisine, servings, difficulty)

if st.session_state.recipe:
    st.subheader("🍽️ Generated Recipe:")
    st.write(st.session_state.recipe)

# ⚠️ Allergy Check
if allergies:
    allergy_list = [a.strip().lower() for a in allergies.split(',')]
    warnings = check_allergies(st.session_state.sanitized_ingredients, allergy_list)
    if warnings:
        st.warning("⚠️ Allergy Alert")
        for w in warnings:
            st.write(f"- {w}")

# 🔄 Substitutions
st.subheader("🔄 Suggested Ingredient Substitutes")
for ing in st.session_state.sanitized_ingredients:
    subs = suggest_substitutes(ing)
    if subs:
        st.write(f"{ing.title()} → {', '.join(subs)}")

# 📅 Meal Plan
if want_meal_plan:
    st.subheader("📅 3-Day Meal Plan")
    meal_plan = plan_meals(st.session_state.sanitized_ingredients, diet_pref, cuisine)
    for day, meals in meal_plan.items():
        st.subheader(f"🗓️ {day}")
        for meal, recipe in meals.items():
            st.write(f"\n🍽️ {meal}:\n{recipe}")

# 🧪 Nutrition Info
total_calories = total_protein = total_carbs = total_fats = 0
if st.session_state.recipe:
    st.subheader("🧪 Nutritional Information")
    for item in st.session_state.sanitized_ingredients:
        data = get_nutrition_data(item)
        if "foods" in data:
            for food in data["foods"]:
                cal = food['nf_calories'] * servings
                prot = food['nf_protein'] * servings
                carb = food['nf_total_carbohydrate'] * servings
                fat = food['nf_total_fat'] * servings
                st.write(f"🔍 {food['food_name'].title()} (x{servings}) - {cal} kcal, {prot}g Protein, {carb}g Carbs, {fat}g Fats")

                total_calories += cal
                total_protein += prot
                total_carbs += carb
                total_fats += fat

# 📊 Nutrition Summary
if st.session_state.recipe:
    st.subheader("📊 Total Nutrition Summary")
    st.write(f"🔥 Calories: {total_calories} kcal")
    st.write(f"💪 Protein: {total_protein} g")
    st.write(f"🍞 Carbs: {total_carbs} g")
    st.write(f"🧈 Fats: {total_fats} g")

# 🛒 Shopping List (Session State)
if st.button("Generate Shopping List"):
    st.session_state.shopping_list = generate_shopping_list(st.session_state.recipe)

if st.session_state.shopping_list:
    st.subheader("🛒 Shopping List:")
    for item in st.session_state.shopping_list:
        st.write(f"- {item}")

# 💾 Save Options (Session State)
save_option = st.radio("Save Recipe", ["None", "Text File", "PDF"], index=0)
filename = st.text_input("Enter filename (without extension)")

if save_option == "Text File" and filename:
    txt_path = save_to_text(filename, st.session_state.recipe)
    if os.path.exists(txt_path):
        st.session_state.saved_file = txt_path  
        st.session_state.success_message_txt = f"✅ Recipe saved as text file: `{txt_path}`"

if save_option == "PDF" and filename:
    pdf_filename = save_to_pdf(filename, st.session_state.recipe)
    if pdf_filename and os.path.exists(pdf_filename):  
        st.session_state.saved_file = pdf_filename  
        st.session_state.success_message_pdf = f"✅ PDF saved successfully: `{pdf_filename}`"

if st.button("Export Schema"):
    if filename:
        schema_filename = f"{filename}.json"
        st.session_state.schema_file = generate_schema(
            recipe_name="Custom Recipe",
            cuisine=cuisine,
            servings=servings,
            prep_time=15,
            cook_time=30,
            ingredients=st.session_state.sanitized_ingredients,
            instructions=st.session_state.recipe.split("\n"),
            nutrition_data={
                "calories": total_calories,
                "protein": total_protein,
                "carbs": total_carbs,
                "fats": total_fats
            },
            filename=schema_filename
        )
        st.session_state.saved_file = schema_filename  
        st.session_state.success_message_schema = f"✅ Schema saved successfully: `{schema_filename}`"

# 📂 Show Success Messages for Saved Files
if st.session_state.success_message_txt:
    st.subheader("📂 Saved File")
    st.success(st.session_state.success_message_txt)

if st.session_state.success_message_pdf:
    st.success(st.session_state.success_message_pdf)

if st.session_state.success_message_schema:
    st.success(st.session_state.success_message_schema)
