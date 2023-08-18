# python_web_scraper_for_cocktails

This Python script scrapes cocktail recipe data from Destination Cocktails. It extracts information such as category, title, link, and image link for each cocktail recipe and saves it to a CSV file.

## Usage
1. Make sure you have Python (3.x) installed.

2. Install the required libraries using pip:

   ```sh
   pip install requests beautifulsoup4
   ```
3. Run the script:

   ```sh
   python pythonscraper.py
   ```

4. The script will retrieve data from the specified URL and save it to a CSV file named cocktails.csv. Each row in the CSV file corresponds to a cocktail recipe and includes the following columns:

- Category: The category of the cocktail.
- Title: The title of the cocktail recipe.
- Link: The link to the cocktail recipe page.
- Image Link: The link to the cocktail recipe image.

## Configuration
You can customize the script by modifying the following variables:

- url: The URL of the page to scrape.
- csv_filename: The name of the CSV file to save the data.

## Requirements
- Python 3.x
- Required libraries: requests, beautifulsoup4

## Disclaimer
Please use this script responsibly and in accordance with the website's terms of use. Be respectful of the website's resources and consider using their APIs if available.

## Author
Yong XIE

## License
This project is licensed under the MIT License.
