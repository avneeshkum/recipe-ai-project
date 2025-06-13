import requests

# Direct API credentials (DO NOT commit these in real-world projects)
NUTRITIONIX_APP_ID = "e8eb6652"
NUTRITIONIX_API_KEY = "8f1fd4f6976a5b982cf1971050428e10"

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
