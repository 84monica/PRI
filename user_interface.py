import json
from unicodedata import category
import requests

# SEARCH
search_url = 'http://localhost:8983/solr/books/select'

title = input("Insert title: ")
#category = input("Insert category: ")

query = {
    'q': 'title:'+title,
}

response = requests.post(search_url, query)

for doc in json.loads(response.text)["response"]["docs"]:
    print("> %s" % (doc['title']))