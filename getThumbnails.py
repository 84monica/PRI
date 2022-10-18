from matplotlib.image import thumbnail
import pandas as pd
import requests
import json

from sqlalchemy import desc

df = pd.read_csv(r'datasets/google_books_1299.csv')  #Importar o csv
print(df)
print("--------------------")

titles = df['title'].tolist() #Criar uma lista com todos os titulos
thumbnail_column = []

count = 0
for searchTerm in titles:
    #Trocar espacos por '+' para fazer a query
    for i in range(len(searchTerm)):
        if searchTerm[i] == ' ':
            searchTerm = searchTerm[:i] + '+' + searchTerm[i+1:]
    #usar a Google Books API
    res = requests.get(url = "https://www.googleapis.com/books/v1/volumes?q=" + searchTerm)
    json_dict = json.loads(res.text)
    #Tenta extrair a thumbnail
    thumb = ""
    try:
        thumb = json_dict['items'][0]['volumeInfo']['imageLinks']['thumbnail']
    except KeyError:
        thumb = "N/A"
    #junta a thumbnail a coluna
    thumbnail_column.append(thumb)
    count+=1
#junta a coluna a df
#guarda df
df["thumbnail"] = thumbnail_column
df.to_csv('1299_complete.csv')
