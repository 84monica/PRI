from matplotlib.image import thumbnail
import pandas as pd
import requests
import json

from sqlalchemy import desc

df = pd.read_csv(r'datasets/google_books_dataset.csv')  #Importar o csv
df2 = pd.read_csv(r'datasets/google_books_1299.csv')
print(df2)
print("--------------------")

titles = df['title'].tolist() #Criar uma lista com todos os titulos
titles2 = df2['title'].tolist()
isbn_column = []  #coluna onde vao ser guardados isbns para adicionar a df
price_column = [] 
currency_column = []
description_column = []
thumbnail_column = []
thumbnail_column_2 = []

count = 0
for search_term in titles2:
    print(" (" + str(count) + "/1298)")
    for i in range(len(search_term)):
        if search_term[i] == ' ':
            search_term = search_term[:i] + '+' + search_term[i+1:]
    thumb = ""
    res = requests.get(url = "https://www.googleapis.com/books/v1/volumes?q=" + search_term)
    json_dict = json.loads(res.text)
    try:
        thumb = json_dict['items'][0]['volumeInfo']['imageLinks']['thumbnail']
    except KeyError:
        thumb = "N/A"
    thumbnail_column_2.append(thumb)
    count+=1

df2["thumbnail"] = thumbnail_column_2
df2.to_csv('dataset_intermidiate_1299.csv')
"""
count = 0
for searchTerm in titles:
    print(" (" + str(count) + "/1024)")
    #Trocar espacos por '+' para fazer a query
    for i in range(len(searchTerm)):
        if searchTerm[i] == ' ':
            searchTerm = searchTerm[:i] + '+' + searchTerm[i+1:]
    #usar a Google Books API
    res = requests.get(url = "https://www.googleapis.com/books/v1/volumes?q=" + searchTerm)
    json_dict = json.loads(res.text)
    #Tenta extrair o isbn
    isbn = ""
    price = 0.0
    currency = ""
    description = ""
    thumb = ""
    not_found_info = True
    not_found_money = True
    items = []
    try:
        items = json_dict['items']
    except KeyError:
        isbn_column.append("0")
        price_column.append(-1)
        currency_column.append("Not for sale")
        description_column.append("N/A")
        thumbnail_column.append("N/A")
        count+=1
        continue
    for item in items:
        type_code = ""
        saleability = ""
        try:
            type_code = item['volumeInfo']['industryIdentifiers'][0]['type']
        except KeyError:
            continue
        try:
            saleability = item['saleInfo']['saleability']
        except KeyError:
            continue
        if (saleability == "FREE") and not_found_money:
            price = 0
            currency = "Free"
            not_found_money = False
        if saleability == "FOR_SALE" and not_found_money:
            try:
                price = float(item['saleInfo']['listPrice']["amount"])
            except KeyError:
                price = -1
            try:
                currency = item['saleInfo']['listPrice']["currencyCode"]
            except KeyError:
                currency = "Not for sale"
            not_found_money = False
        if ((type_code == "ISBN_10" or type_code == "ISBN_13") and not_found_info):
            try:
                isbn = item['volumeInfo']['industryIdentifiers'][0]['identifier']
            except KeyError:
                isbn = "0"
            try:
                description = item['volumeInfo']['description']
            except KeyError:
                description = "N/A"
            try:
                thumb = item['volumeInfo']['imageLinks']['thumbnail']
            except KeyError:
                thumb = "N/A"
            not_found_info = False
        
    if not_found_info:
        try:
            isbn = items[0]['volumeInfo']['industryIdentifiers'][0]['identifier']
        except KeyError:
            isbn = "0"
        try:
            description = items[0]['volumeInfo']['description']
        except KeyError:
            description = "N/A"
        try:
            thumb = items[0]['volumeInfo']['imageLinks']['thumbnail']
        except KeyError:
            thumb = "N/A"
    if not_found_money:
        try:
            price = float(items[0]['saleInfo']['listPrice']["amount"])
        except KeyError:
            price = -1
        try:
            currency = items[0]['saleInfo']['listPrice']["currencyCode"]
        except KeyError:
            currency = "Not for sale"
    #junta o isbn a coluna
    isbn_column.append(isbn)
    price_column.append(price)
    currency_column.append(currency)
    description_column.append(description)
    thumbnail_column.append(thumb)
    count+=1
#junta a coluna a df
#guarda df
print("")
df["isbn"] = isbn_column
df["price"] = price_column
df["currency"] = currency_column
df["description"] = description_column
df["thumbnail"] = thumbnail_column
df.to_csv('dataset_intermidiate.csv')
"""