import requests
from bs4 import BeautifulSoup

# Step 1: Read "category_links.txt" file
with open("category_links.txt", "r", encoding="utf-8") as file:
    category_links = file.read().splitlines()

# Step 3-6: Process each link
allLinks = []
for link in category_links:
    # Step 4: Send GET request to link
    response = requests.get(link)
    if response.status_code == 200:
        html_content = response.text

        # Step 5: Search for <h2> with class="entry-title"
        soup = BeautifulSoup(html_content, "html.parser")
        h2_entries = soup.find_all("h2", class_="entry-title")

        # Step 6: Append href values from <a> within <h2> to allLinks list
        for h2_entry in h2_entries:
            a_tags = h2_entry.find_all("a")
            for a_tag in a_tags:
                href = a_tag.get("href")
                if href:
                    allLinks.append(href)
    else:
        print(f"Failed to retrieve data from {link}")

# Step 7: Write allLinks contents to "all_products.txt" file
with open("all_products.txt", "w", encoding="utf-8") as file:
    for link in allLinks:
        file.write(link + "\n")

print("Links written to all_products.txt file.")
