📘 API Documentation (README/Markdown Version)

# 📘 API Documentation – AI-Powered Recipe Generator

## 🔧 Project Modules Overview

| Module              | Description |
|---------------------|-------------|
| `main.py`           | Main CLI interface |
| `generator.py`      | Recipe generation using Cohere LLM |
| `nutrition.py`      | Nutritional info using Nutritionix API |
| `substitutions.py`  | Suggest ingredient replacements |
| `meal_planner.py`   | 3-day meal planning |
| `shopping_list.py`  | Extracts ingredients into shopping list |
| `saver_recipe.py`   | Saves recipe in TXT/PDF formats |
| `utils/sanitizer.py`| Ingredient cleaner |
| `utils/allergy_checker.py` | Allergy filter |

---

## 🧠 AI Model
- Uses **Cohere Command-R+** model via `generator.py`
- Prompt is dynamically formed using:
  - Ingredients
  - Dietary preference
  - Cuisine
  - Servings
  - Difficulty level

---

## 🧪 Nutrition API
- **Nutritionix API** (natural language endpoint)
- Input: `aloo, onion, rice`
- Output: JSON with `calories`, `protein`, `carbs`, `fats`

```python
data = get_nutrition_data("1 cup rice")
print(data['foods'][0]['nf_calories'])


📤 Input Parameters
Prompt	Description
Ingredients	Comma-separated list
Dietary Preference	veg / vegan / keto / etc.
Cuisine	Indian / Chinese / etc.
Difficulty	easy / medium / hard
Servings	Default is 1
Allergies	Filter ingredients

📥 Output
Step-by-step recipe

Nutrition summary

Substitution suggestions

Shopping list

Save options: .txt, .pdf

3-day meal plan if selected


💾 Sample File Structure

📁 ai_recipe_project/
│
├── main.py
├── generator.py
├── nutrition.py
├── substitutions.py
├── meal_planner.py
├── shopping_list.py
├── saver_recipe.py
├── sample_recipes/
│   ├── paneer_recipe.txt
│   ├── aloo_gobi.pdf
│   └── ...
└── utils/
    ├── sanitizer.py
    └── allergy_checker.py


🧪 Sample Nutritionix API Response
json
Copy
Edit
{
  "foods": [
    {
      "food_name": "rice",
      "nf_calories": 206,
      "nf_protein": 4.25,
      "nf_total_carbohydrate": 44.51,
      "nf_total_fat": 0.44
    }
  ]
}


🛠️ Tech Stack
Python 3.11

Cohere AI (LLM)

Nutritionix API

FPDF for PDF generation

CLI-based interaction

