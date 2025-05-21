import pandas as pd


url='https://en.wikipedia.org/wiki/List_of_countries_by_GDP_(nominal)'

tables = pd.read_html(url)

print(f'Total tables found : {len(tables)}')

df= tables[0]
print(df.head())

df.to_csv('gdp_data.csv', index=False)