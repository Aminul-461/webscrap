import requests as re
from bs4 import BeautifulSoup as bs

url='https://books.toscrape.com/catalogue/page-1.html'
response=re.get(url)
soup=bs(response.text,'html.parser')

books=soup.find_all('article', class_='product_pod')

for book in books:
      title=book.h3.a['title']
      price=book.find('p', class_='instock avalilability').text.strip()
      rating=book.p['classs'][1]

      print(f'Title: {title}')
      print(f'price: {price}')
      print(f'Rating: {rating}\n')

 