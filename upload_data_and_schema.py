import json
import requests

# IMPORT SCHEMA AND DATAFILES
schema_file = open('schema.json')
books_file = open('final_books_dataset.json')

schema_json = json.load(schema_file)
books_json = json.load(books_file)

schema_url = 'http://localhost:8983/solr/books/schema'
upload_data_url = 'http://localhost:8983/solr/books/update?commit=true'

x = requests.post(schema_url, json = schema_json)
print(x.text)
x = requests.post(upload_data_url, json = books_json)
print(x.text)

schema_file.close()
books_file.close()