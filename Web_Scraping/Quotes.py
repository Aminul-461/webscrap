import requests as re
from bs4 import BeautifulSoup as bs


 # send a request to the website

url='https://quotes.toscrape.com'
response=re.get(url)

# parse the html content

soup=bs(response.text, 'html.parser')

# Extract quates and authers
quotes=soup.find_all('div', class_='quote')

for quote in quotes:
      text=quote.find('span', class_='text').text
      author=quote.find('small',class_='author').text
      print(f'{text}-{author}')