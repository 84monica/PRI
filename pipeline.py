import pandas as pd
import requests
import json

df = pd.read_csv(r'google_books_dataset.csv')  #Importar o csv
print(df)
print("--------------------")

titles = df['title'].tolist() #Criar uma lista com todos os titulos
isbn_column = []  #coluna onde vao ser guardados isbns para adicionar a df
count = 0
for searchTerm in titles:
    print("ISBN of book " + searchTerm + ": ", end="")
    #Trocar espacos por '+' para fazer a query
    for i in range(len(searchTerm)):
        if searchTerm[i] == ' ':
            searchTerm = searchTerm[:i] + '+' + searchTerm[i+1:]
    #usar a Google Books API
    res = requests.get(url = "https://www.googleapis.com/books/v1/volumes?q=" + searchTerm)
    json_dict = json.loads(res.text)
    #Tenta extrair o isbn
    isbn = ""
    try:
        isbn = json_dict['items'][0]['volumeInfo']['industryIdentifiers'][0]['identifier']
    except KeyError:
        isbn = "0"
    print(isbn + " (" + str(count) + "/1024)")
    #junta o isbn a coluna
    isbn_column.append(isbn)
    count+=1
#junta a coluna a df
#guarda df
df["isbn"] = isbn_column
df.to_csv('google_books_dataset_isbn.csv')