import os
import json
import requests
from bs4 import BeautifulSoup

def parse_product_info(url):
    # Send a GET request to the URL
    response = requests.get(url)

    # Parse the response content as HTML
    soup = BeautifulSoup(response.content, 'html.parser')

    # Create a JSON object with the required information
    product_info = {}
    product_info['name'] = soup.find('div', {'class': 'h1'}).text.strip()
    product_info['desc'] = soup.findAll('div', {'class': 'content'})[1].find('p').text.strip()
    product_info['techs'] = soup.find('div', {'id': 'technicalAspects'}).find('div', {'class': 'col-md-12'}).find('p').text.strip()
    product_info['shelf'] = soup.find('div', {'id': 'terminToEat'}).find('div', {'class': 'col-md-12'}).find('p').text.strip()
    product_info['packaging'] = soup.find('div', {'id': 'package'}).find('div', {'class': 'col-md-12'}).find('p').text.strip()
    product_info['applications'] = soup.find('div', {'id': 'application'}).find('div', {'class': 'col-md-12'}).find('p').text.strip()

    return product_info

def main():
    # Read the 'all_products.txt' file
    with open('all_products.txt', 'r') as f:
        links = f.readlines()

    # Strip whitespace characters like `\n` at the end of each line
    links = [link.strip() for link in links]

    # Ensure the data directory exists
    if not os.path.exists('data'):
        os.makedirs('data')

    # Iterate over each URL
    i = 0
    for url in links:
        i+=1
        # Parse the product info from the URL
        product_info = parse_product_info(url)

        # Write the product info to a new .txt file in the data directory
        with open(f'data/products/{product_info["name"]}.json', 'w', encoding='utf-8') as f:
            f.write(json.dumps(product_info, indent=4).encode('utf-8').decode('unicode_escape'))
        print(f'"{product_info["name"]}" is done! {i}/{len(links)}')

if __name__ == '__main__':
    main()
