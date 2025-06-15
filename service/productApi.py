import requests

def fetch_product_details():
    try:
        response = requests.get("http://127.0.0.1:8000/products")
        if response.status_code == 200:
            return response.json()
        else:
            return "No more products here :("
    except Exception as e:
        return {"error": str(e)}