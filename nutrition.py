# nutrition.py
import requests
import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

NUTRITIONIX_APP_ID = os.getenv("NUTRITIONIX_APP_ID")
NUTRITIONIX_API_KEY = os.getenv("NUTRITIONIX_API_KEY")

BASE_URL = "https://trackapi.nutritionix.com/v2/natural/nutrients"

def get_nutrition_data(ingredient_text):
    """
    Fetch nutritional data for a given list of ingredients using Nutritionix API.

    Args:
        ingredient_text (str): e.g. "1 cup rice, 100g paneer, 1 potato"

    Returns:
        dict: Nutrition data including calories, macros, etc.
    """
    headers = {
        "x-app-id": NUTRITIONIX_APP_ID,
        "x-app-key": NUTRITIONIX_API_KEY,
        "Content-Type": "application/json"
    }

    data = {
        "query": ingredient_text,
        "timezone": "Asia/Kolkata"
    }

    response = requests.post(BASE_URL, json=data, headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        return {
            "error": f"Failed to fetch data. Status code: {response.status_code}",
            "details": response.text
        }
