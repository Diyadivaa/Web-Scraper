import requests
import csv
from lxml import html

# Open a CSV file for writing
with open('quotes.csv', 'w', newline='', encoding='utf-8-sig') as csvfile:
    # Create a CSV writer
    writer = csv.writer(csvfile)
    
    # Write the header row
    writer.writerow(['Quote', 'Author'])
    
    # Set the base URL of the website
    base_url = 'http://quotes.toscrape.com'
    
    # Set the starting URL
    url = '/page/1/'
    
    # Set the XPath to the quotes
    xpath = '//div[@class="quote"]'
    
    # Set the XPath to the next button
    next_button_xpath = '//li[@class="next"]/a'
    
    # Scrape the quotes from each page
    while True:
        # Send an HTTP request to the current URL
        response = requests.get(base_url + url)

        # Parse the HTML content of the page
        doc = html.fromstring(response.content)

        # Extract the quotes
        quotes = doc.xpath(xpath)

        # Write the quotes to the CSV file
        for quote in quotes:
            text = quote.xpath('.//span[@class="text"]/text()')[0]
            author = quote.xpath('.//small[@class="author"]/text()')[0]
            writer.writerow([text, author])
        
        # Check if there is a next button
        next_button = doc.xpath(next_button_xpath)
        if not next_button:
            # If there is no next button, stop the loop
            break
        
        # Get the URL of the next page
        url = next_button[0].attrib['href']
        
