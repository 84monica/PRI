from matplotlib.image import thumbnail
import pandas as pd
import requests
import json

from sqlalchemy import desc

df = pd.read_csv(r'datasets/google_books_dataset.csv')  #Importar o csv
print(df)
print("--------------------")

titles = df['title'].tolist() #Criar uma lista com todos os titulos
isbn_column = []  #coluna onde vao ser guardados isbns para adicionar a df
price_column = [] 
currency_column = []
description_column = []
thumbnail_column = []

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
    try:
        isbn = json_dict['items'][0]['volumeInfo']['industryIdentifiers'][0]['identifier']
    except KeyError:
        isbn = "0"
    try:
        price = float(json_dict['items'][0]['salesInfo']['listPrice']["amount"])
    except KeyError:
        price = -1
    try:
        currency = json_dict['items'][0]['salesInfo']['listPrice']["currencyCode"]
    except KeyError:
        currency = "N/A"
    try:
        description = json_dict['items'][0]['volumeInfo']['description']
    except KeyError:
        description = "N/A"
    try:
        thumb = json_dict['items'][0]['volumeInfo']['imageLinks']['thumbnail']
    except KeyError:
        thumb = "N/A"
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
