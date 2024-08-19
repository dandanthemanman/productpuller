import requests
import os
from dotenv import load_dotenv
import requests
import openai
from io import BytesIO
from PIL import Image
import base64

# Load the .env file
load_dotenv()

SHOPIFY_SHOP_NAME = os.getenv('SHOPIFY_SHOP_NAME')
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

openai.api_key = OPENAI_API_KEY

def generate_image_prompt(description):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are an AI that generates image descriptions."},
            {"role": "user", "content": f"Generate an image description based on this product description: {description}"}
        ]
    )
    return response['choices'][0]['message']['content'].strip()

sample_description = "A stylish black leather bag with silver accents."

print (generate_image_prompt(sample_description))
