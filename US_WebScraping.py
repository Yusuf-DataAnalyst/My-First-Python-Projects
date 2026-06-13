from bs4 import BeautifulSoup
import requests
url = 'https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}
page = requests.get(url,headers=headers)
soup = BeautifulSoup(page.text,'html')
print (soup)
soup.find_all('table')[1]
soup.find('table', class_= 'Wikitable sortable')
table.find_all('th')
print (table)
word_titles = table.find_all('th')
word_table_titles = [title.text.strip() for title in  word_titles]
print (word_table_titles)
import pandas as pd
df = pd.DataFrame(columns = word_table_titles)
df
column_data = table.find_all('tr')
for row in column_data [1:]:
    row_data = row.find_all('td')
    individual_row_data = [data.text.strip() for data in  row_data]
    lenght = len(df)
    df.loc [lenght] = individual_row_data


df.to_csv(r'C:\Users\nexora Technology\OneDrive\New folder/companies.csv',index = False)
