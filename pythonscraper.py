import requests
from bs4 import BeautifulSoup
import csv

url = 'https://www.destinationcocktails.fr/liste-de-recettes-de-cocktails-par-thematiques/'  # Replace with the actual URL
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Open the CSV file for writing
    with open('cocktails.csv', 'w', newline='', encoding='utf-8') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(['Category', 'Title', 'Link', 'Image Link'])  # Write header
        
        # Find all the recette blocks
        recette_blocks = soup.find_all('div', class_='recette-block')
        
        # Loop through each recette block
        for recette_block in recette_blocks:
            title = recette_block.find('h2', class_='title')
            
            if title:
                category = title.text  # Use the title as the category
            else:
                category = "Unknown"
            
            col_recettes = recette_block.find_all('div', class_='col-recette')
            for col_recette in col_recettes:
                if col_recette:
                    link = col_recette.find('a')['href']
                    img_link = col_recette.find('img')['src']
                    recette_title = col_recette.find('h3', class_='recette-titre').text.strip()
                    
                    # Write data to CSV file
                    csvwriter.writerow([category, recette_title, link, img_link])
                else:
                    print("col-recette not found within the recette block.")
else:
    print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
