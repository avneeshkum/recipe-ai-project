🧑‍🍳 AI-Powered Recipe Generator (CLI + UI)

A smart, AI-powered recipe generator that creates personalized and nutritious recipes based on user-selected ingredients. Now available in both Command-Line and Streamlit UI formats, this application seamlessly integrates allergy detection, ingredient substitutions, nutrition analysis, shopping lists, and PDF exports, making healthy eating more accessible!

📌 Key Features
✅ AI-based Recipe Generation: Enter ingredients and get tailored recipes instantly ⚠️ Allergy Detection: Alerts users if any entered ingredients may cause allergic reactions 🔁 Smart Substitutions: Suggests alternative ingredients for dietary needs 🧪 Advanced Nutrition Analysis: Provides calorie, protein, carbohydrate, and fat breakdowns using Nutritionix API 🛒 Auto-Generated Shopping List: Saves time by compiling required ingredients into a structured list 📄 Save Recipes as Text & PDF: Export recipes in a clean, formatted .txt or .pdf file 🍽️ Dietary Preferences Support: Choose Veg, Vegan, Keto, Gluten-Free, or Custom Diets 🖥️ Streamlit UI Version: Fully interactive recipe generator with intuitive buttons & form inputs 🧑‍💻 CLI Version: Lightweight, fast command-line interaction

🚀 How to Run
💻 CLI Version
1️⃣ Install Dependencies:

bash
pip install -r requirements.txt
2️⃣ Run CLI Recipe Generator:

bash
python main.py
3️⃣ Follow the Prompts:

Enter ingredients

Select diet, cuisine & servings

Get a fully AI-generated recipe

View nutrition breakdown & shopping list

Save recipe as .txt or .pdf

🖥️ Streamlit UI Version
1️⃣ Install Streamlit (if not installed):

bash
pip install streamlit
2️⃣ Run UI Recipe Generator:

bash
streamlit run app.py
3️⃣ Interact via Web Interface:

Input ingredients in text fields

Choose preferences via dropdowns

Generate recipe & nutrition summary

Save as PDF, Text, or Schema

🛠️ Project Structure
php
Recipe-Generator/
├── main.py             # CLI-based recipe generator  
├── app.py              # Streamlit UI-based recipe generator  
├── generator.py        # AI-powered recipe generation logic  
├── nutrition.py        # Nutrition API handler (calories, macros)  
├── substitutions.py    # Ingredient substitution logic  
├── meal_planner.py     # 3-day meal planner functionality  
├── shopping_list.py    # Shopping list generator  
├── saver_recipe.py     # Saves recipes as .txt or styled .pdf  
├── utils/  
│   ├── sanitizer.py    # Cleans ingredient input  
│   └── allergy_checker.py  # Detects allergens & warnings  
├── requirements.txt    # Dependencies  
└── README.md           # Project documentation  
🔌 APIs & Libraries Used
Nutritionix API – Real-time nutritional data retrieval

FPDF – PDF generation for formatted recipe exports

Requests – Handling API interactions

Streamlit – Interactive UI framework for web-based functionality

📹 Demo Video
🔗 [Attach recorded demo video link here] (Recommended for GitHub or internship submission)

🙋‍♂️ Author
👤 Avneesh Kumar 🎓 MCA Student | AI & Web Development Enthusiast

📌 GitHub: Avneesh Kumar 📌 LinkedIn: Avneesh Kumar

📌 Project Note
Developed as part of an internship assignment, this project showcases expertise in Python, API integration, AI-powered recipe generation, and interactive web applications.


