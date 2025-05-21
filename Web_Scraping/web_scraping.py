import requests as re
from bs4 import BeautifulSoup as bs
#Fetch th Web page

# url= 'https://example.com' 

response = re.get(url)
print(response.status_code)
print(response.text)

# # Parse the HTMl
soup= bs(response.text,'html.parser')
print(soup.prettify())

# #Extract data(Heading,paragraphs,Links)
 
# # GET the first heading
heading=soup.find('h1')
print(heading.text)

# #get all pragraph
paragraph=soup.find_all('p')

for para in paragraph:
      print(para.text)

# # Get all links
links=soup.find_all('a')
for link in links:
      print(link.get('href'))


url='https://www.bbc.com/news'

response=re.get(url)
soup=bs(response.text,'html.parser')


headlines= soup.find_all('h3')
for headline in headlines:
      print(headline.text.strip())



 
