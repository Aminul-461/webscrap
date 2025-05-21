
import csv

import requests as re 
from bs4 import BeautifulSoup as bs


# send the request to the website
url='http://quotes.toscrape.com'

response= re.get(url)


# parse the page content
soup=bs(response.text,'html.parser')

# Find all quates on the page
quotes=soup.find_all('div',class_='quote')

with open('quotes.csv','w',newline='', encoding='utf-8') as file:
      writer = csv.writer(file)
      writer.writerow(['Quote', 'Author'])

      for quote in quotes:

         text=quote.find('span', class_= 'text').text
         author=quote.find('small', class_='author').text
         writer.writerow([text,author])

print("Quotes have been succeessffuully saved  to  quotes.csv")

