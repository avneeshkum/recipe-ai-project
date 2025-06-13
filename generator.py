# generator.py
import cohere
import os
from dotenv import load_dotenv

load_dotenv()  # Load from .env file

COHERE_API_KEY = os.getenv("COHERE_API_KEY")
co = cohere.Client(COHERE_API_KEY)

def generate_recipe(ingredients, dietary_preference=None, cuisine=None, servings=1, difficulty="medium"):
    prompt = f"""
You are a professional chef AI. Create a detailed and customized recipe using the following:

Ingredients:
{', '.join(ingredients)}

Recipe Requirements:
- Follow dietary preference: {dietary_preference or 'None'}
- Cuisine style: {cuisine or 'Any'}
- Difficulty level: {difficulty or 'medium'}
- The recipe must be for exactly {servings} serving(s)
- Scale ingredient quantities realistically based on the number of servings
- Include only common spices and essential pantry items if needed

Output Format:
1. **Recipe Name**
2. **Preparation Time**
3. **Cooking Time**
4. **Number of Servings**: (must be exactly {servings})
5. **Ingredients List** (with proper quantity and units scaled to servings)
6. **Step-by-step Cooking Instructions**
7. **Serving Suggestions**

Be practical, avoid exotic ingredients unless necessary, and generate only the recipe — no explanations.
    """

    try:
        response = co.generate(
            model="command-r-plus",
            prompt=prompt.strip(),
            max_tokens=1000,
            temperature=0.7
        )
        return response.generations[0].text.strip()
    except Exception as e:
        return f"❌ Cohere API Error: {str(e)}"
