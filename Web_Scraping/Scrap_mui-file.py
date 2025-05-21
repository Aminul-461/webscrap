import requests as re

from bs4 import BeautifulSoup as bs
import csv


base_url='https://quotes.toscrape.com/page/{}'


with  open('all_quotes.csv','w', newline='', encodinng='utf-8') as file:
      writer=csv.writer(file)
      writer.writerow(['Quote','Author'])

for page in range(1,11):
      url=base_url.format(page)
      response=re.get(url)
      soup=bs(response.text,'html.parser')

      quotes=soup.find_all('div', class_='quote')

      if not quotes:
            break

      for quote in quotes:
            text=quote.find('span',class_='text').text
            author=quote.find('small',class_='author').text
            writer.writerow([text,author])

