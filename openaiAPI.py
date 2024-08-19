import requests
import os
from dotenv import load_dotenv
import requests
from openai import OpenAI
from io import BytesIO
from PIL import Image
import base64

# Load the .env file
load_dotenv()

SHOPIFY_SHOP_NAME = os.getenv('SHOPIFY_SHOP_NAME')
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

client = OpenAI(api_key=OPENAI_API_KEY)

def generate_image_prompt(description):
    response = client.chat.completions.create(model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are an AI that generates image descriptions."},
        {"role": "user", "content": f"Generate an image description based on this product description: {description}"}
    ])
    return response.choices[0].message.content.strip()

sample_description = "A stylish black leather bag with silver accents."

print (generate_image_prompt(sample_description))

