# 📘️ API Documentation – AI-Powered Recipe Generator

## 🔧 Project Modules Overview

| Module                     | Description                                  |
| -------------------------- | -------------------------------------------- |
| `main.py`                  | CLI interface to interact with recipe engine |
| `generator.py`             | Handles AI recipe generation via Cohere API  |
| `nutrition.py`             | Retrieves nutrition data using Nutritionix   |
| `substitutions.py`         | Suggests ingredient replacements             |
| `meal_planner.py`          | Builds optional 3-day meal plans             |
| `shopping_list.py`         | Extracts ingredients into shopping list      |
| `saver_recipe.py`          | Saves recipes as `.txt` or styled `.pdf`     |
| `utils/sanitizer.py`       | Cleans and normalizes ingredient input       |
| `utils/allergy_checker.py` | Detects common allergens from input          |

---

## 🧠 AI Model

* Uses **Cohere Command-R+** model for natural recipe generation.
* Prompt is dynamically constructed with:

  * User-input ingredients
  * Dietary preference
  * Cuisine type
  * Number of servings
  * Difficulty level

---

## 🧪 Nutrition Analysis via Nutritionix API

* **Nutritionix Natural Language API**
* Input Example: `aloo, onion, rice`
* Output: Calorie and macronutrient breakdown (JSON format)

### Sample Code:

```python
from nutrition import get_nutrition_data

data = get_nutrition_data("1 cup rice")
print(data['foods'][0]['nf_calories'])
```

---

## 📄 Input Parameters

| Parameter          | Description                            |
| ------------------ | -------------------------------------- |
| Ingredients        | Comma-separated list (e.g., rice, dal) |
| Dietary Preference | veg, vegan, keto, etc.                 |
| Cuisine            | Indian, Chinese, Italian, etc.         |
| Difficulty         | easy, medium, hard                     |
| Servings           | Number of servings (default: 1)        |
| Allergies          | Exclude allergens (nuts, gluten...)    |

---

## 📥 Output Summary

* **Step-by-step AI-generated recipe**
* **Nutrition breakdown** (calories, protein, fats, carbs)
* **Smart substitutions** (if needed)
* **Auto-generated shopping list**
* **Export options**: `.txt`, `.pdf`, or `.json`
* **Optional meal planner**: 3-day plan

---

## 🗂️ Sample File Structure

```
ai_recipe_project/
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
│   └── schemas/
│       └── recipe.json
└── utils/
    ├── sanitizer.py
    └── allergy_checker.py
```

---

## 🧪 Sample Nutritionix API JSON Response

```json
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
```

---

## 🛠️ Tech Stack

* Python 3.11
* Cohere LLM API (Command-R+)
* Nutritionix Natural Language API
* FPDF (for recipe PDF export)
* Requests (API calls)
* Streamlit (UI)
* CLI (Command Line Interface)

---

## 📅 Documentation Location

* API & logic docs: `docs/api_documentation.md`
* Dietary reference: `docs/dietary_guide.md`
* Recipe schemas: `sample_recipes/schemas/recipe.json`
