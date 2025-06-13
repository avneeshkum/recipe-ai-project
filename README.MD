# 🧑‍🍳 AI-Powered Recipe Generator CLI

A powerful command-line application that generates smart, healthy, and personalized recipes using AI and Nutrition APIs.

## 📌 Features

- ✅ Ingredient-based recipe generation using AI
- ⚠️ Allergy detection with warnings
- 🔁 Suggests ingredient substitutions
- 🧪 Nutrition analysis using Nutritionix API
- 🛒 Auto-generated shopping list
- 📄 Save recipes as `.txt` or beautifully styled `.pdf`
- 🍽️ Supports dietary preferences (veg, vegan, keto, etc.)
- 🧑‍💻 CLI-based — fast and simple interaction

---

## 🚀 How to Run

1. **Install Python packages**:
   ```bash
   pip install -r requirements.txt
Run the app:

bash
Copy
Edit
python main.py
Follow the prompts to:

Enter ingredients

Choose diet, cuisine, servings, allergies

Get recipe, nutrition info, and shopping list

🛠️ Project Structure
php
Copy
Edit
Recipe-Generator-CLI/
├── main.py                  # Main interface
├── generator.py             # Recipe generation logic
├── nutrition.py             # Nutrition API handler
├── substitutions.py         # Substitution logic
├── meal_planner.py          # 3-day meal planner
├── shopping_list.py         # Shopping list generator
├── saver_recipe.py          # Save as .txt / .pdf
├── utils/
│   ├── sanitizer.py         # Cleans ingredient input
│   └── allergy_checker.py   # Allergy detection
├── requirements.txt
└── README.md

🔌 APIs & Libraries Used
Nutritionix API – For real-time nutrition data

FPDF – For PDF generation

Requests – For HTTP requests

📹 Demo Video
🔗 [Attach your recorded demo video link here if submitting on GitHub or internship portal]

🙋‍♂️ Author
Avneesh Kumar
MCA Student | AI & Web Dev Enthusiast
GitHub: https://github.com/avneeshkum
LinkedIn:https://www.linkedin.com/in/avneesh-kumar/

📌 Note
This project was developed as part of an internship assignment to demonstrate skills in Python, API integration, and basic AI logic for recipe generation.