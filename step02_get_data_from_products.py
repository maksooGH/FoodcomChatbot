import os
import json
import requests
from bs4 import BeautifulSoup

# Load the links
with open('all_products.txt', 'r', encoding='utf-8') as f:
    links = [line.strip() for line in f]

# Main list
products = []

i = 0
for link in links:
    i+=1
    print(f'{link} [{i}]')
    # GET request
    response = requests.get(link)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Create empty product dictionary
    product = {'name': '', 'description': ''}

    # Find meta tags
    title_tag = soup.find('meta', {'property': 'og:title'})
    description_tag = soup.find('meta', {'property': 'og:description'})

    # Extract and assign name and description
    if title_tag and 'content' in title_tag.attrs:
        product['name'] = title_tag['content'].split(' | ')[0]
    if description_tag and 'content' in description_tag.attrs:
        product['description'] = description_tag['content']

    # Append the product to the list
    products.append(product)
    print(f"done {i}")
# Write to file
os.makedirs('data', exist_ok=True)
with open('data/foodcom_products.json', 'w', encoding='utf-8') as f:
    json.dump(products, f, ensure_ascii=False)
