from bs4 import BeautifulSoup
import requests
url= 'https://books.toscrape.com/'
page=requests.get(url)
soup= BeautifulSoup(page.text,'html.parser')
title = first_book.h3.a['title']
price = first_book.find('p',class_='price_color').text
print (title)
print (price)
all_books = soup.find_all('article',class_= 'product_pod')
for book in all_books:
    book_title = book.h3.a['title']
    book_price= book.find('p',class_='price_color').text
    print(f' : {book_title} |  : {book_price}')
