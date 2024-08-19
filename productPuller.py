import requests
import os
from dotenv import load_dotenv

# Load the .env file
load_dotenv()

# Access the environment variables
SHOPIFY_API_KEY = os.getenv('SHOPIFY_API_KEY')
SHOPIFY_API_PASSWORD = os.getenv('SHOPIFY_API_PASSWORD')
SHOPIFY_SHOP_NAME = os.getenv('SHOPIFY_SHOP_NAME')
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

# URL for the API endpoint
url = f"https://{SHOPIFY_API_KEY}:{SHOPIFY_API_PASSWORD}@{SHOPIFY_SHOP_NAME}.myshopify.com/admin/api/2023-07/products.json"

response = requests.get(url)
    
# Check if the request was successful
if response.status_code == 200:
    products = response.json()['products']
    for product in products:
        print(product['title'])
else:
    print("Failed to retrieve products", response.status_code)
