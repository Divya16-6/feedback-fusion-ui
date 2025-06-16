import requests
from config import BASE_URL

def fetch_product_details():
    try:
        response = requests.get(f"{BASE_URL}/products")
        if response.status_code == 200:
            return response.json()
        else:
            return "No more products here :("
    except Exception as e:
        return {"error": str(e)}